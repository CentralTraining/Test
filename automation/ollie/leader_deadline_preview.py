"""Send one explicitly requested deadline preview to the configured leader only."""
import argparse
import asyncio
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import time

from daily_digest import MarkdownMessage, format_deadline_digest, given_name
from deadline_scheduler import sync_deadlines
from github_daily import GitHubState, StateError, validate_configuration
from kpi import KpiSourceError
from tracker import DeliveryError, DingTalkSender, Tracker


def validate_request(request, now):
    if not isinstance(request, dict) or set(request) != {'request_id', 'requested_at', 'source'}:
        raise StateError('invalid_preview_request')
    if request['source'] != 'leader-deadline-preview' or not re.fullmatch(r'[a-f0-9-]{36}', str(request['request_id'])):
        raise StateError('invalid_preview_request')
    try:
        requested = datetime.fromisoformat(request['requested_at'].replace('Z', '+00:00'))
        if requested.tzinfo is None or not -300 <= now - requested.timestamp() <= 3600: raise ValueError()
    except (ValueError, TypeError, AttributeError):
        raise StateError('stale_or_invalid_preview_request') from None
    return request['request_id']


def preview_content(tracker, now):
    # The leader's normal digest covers the Team. Do not create sample assignments,
    # KPI jobs, alerts, group jobs or scheduled sends for any Trainer.
    rows = [row for row in tracker.pending_tasks() if row[2] > now]
    tasks = tracker.group_tasks(rows)
    if tasks:
        content = format_deadline_digest(tracker.name(tracker.owner), tasks, now)
    else:
        content = MarkdownMessage(f'Xin chào {given_name(tracker.name(tracker.owner))}!\n\n📌 Hiện không có công việc còn hạn cần nhắc.')
    if len(content.encode('utf-8')) > 18000: raise StateError('preview_message_too_large')
    return content, len(tasks)


def send_once(database, tracker, sender, store, request_id, content, task_count, now):
    database.execute('''CREATE TABLE IF NOT EXISTS leader_deadline_previews (
        request_id TEXT PRIMARY KEY, status TEXT NOT NULL, receipt TEXT,
        task_count INTEGER NOT NULL, updated_at REAL NOT NULL)''')
    existing = database.execute('SELECT status,receipt,task_count FROM leader_deadline_previews WHERE request_id=?', (request_id,)).fetchone()
    if existing:
        status, receipt, count = existing
        return {'mode': 'leader_deadline_preview', 'accepted': int(status == 'accepted' and bool(receipt)),
                'failed': int(status == 'failed'), 'uncertain': int(status in ('sending', 'unknown')),
                'task_count': count, 'already_recorded': True, 'group_accepted': 0, 'trainer_accepted': 0}
    database.execute('INSERT INTO leader_deadline_previews VALUES (?,\'sending\',NULL,?,?)', (request_id, task_count, now))
    database.commit()
    store.save(database)  # Persist the guard before making the single recipient request.
    try:
        receipt = sender.send('dm', tracker.owner, content)
        if not receipt: raise DeliveryError('missing_send_receipt', ambiguous=True)
    except DeliveryError as error:
        status = 'unknown' if error.ambiguous else 'failed'
        database.execute('UPDATE leader_deadline_previews SET status=?,updated_at=? WHERE request_id=?', (status, now, request_id))
        database.commit()
        store.save(database)
        return {'mode': 'leader_deadline_preview', 'accepted': 0, 'failed': int(status == 'failed'),
                'uncertain': int(status == 'unknown'), 'task_count': task_count,
                'group_accepted': 0, 'trainer_accepted': 0}
    database.execute("UPDATE leader_deadline_previews SET status='accepted',receipt=?,updated_at=? WHERE request_id=?", (receipt, now, request_id))
    database.commit()
    store.save(database)
    return {'mode': 'leader_deadline_preview', 'accepted': 1, 'failed': 0, 'uncertain': 0,
            'task_count': task_count, 'receipt_confirmed': True, 'group_accepted': 0, 'trainer_accepted': 0}


async def run(config, request, now=None):
    now = time.time() if now is None else now
    request_id = validate_request(request, now)
    validate_configuration(config)
    store = GitHubState(os.environ.get('GITHUB_REPOSITORY', ''), os.environ.get('GITHUB_TOKEN', ''),
                        config.get('ledger_key', ''), os.environ.get('GITHUB_SHA', ''))
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'preview.sqlite3'
        store.restore(path)
        database = sqlite3.connect(path)
        try:
            tracker = Tracker(database, config['state'])
            await sync_deadlines(tracker, config, now)
            content, count = preview_content(tracker, now)
            result = send_once(database, tracker, DingTalkSender(config['credentials'], config['state']), store,
                               request_id, content, count, now)
            print(json.dumps(result))  # Only counters; never bodies, identities, tokens or receipt keys.
            return not (result['accepted'] == 1 and not result['failed'] and not result['uncertain'])
        finally:
            database.close()


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser()
    parser.add_argument('--request-file', required=True)
    args = parser.parse_args()
    try:
        request = json.loads(Path(args.request_file).read_text())
        config = json.loads(os.environ.get('OLLIE_KPI_CONFIG_JSON', ''))
        return int(asyncio.run(run(config, request)))
    except Exception as error:
        # A pending send guard remains in the encrypted state on interruption.
        print(json.dumps({'mode': 'leader_deadline_preview', 'confirmed': False, 'error_type': type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
