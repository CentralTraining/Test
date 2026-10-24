from datetime import datetime, timezone
import sqlite3
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from daily_digest import MarkdownMessage
from github_daily import StateError
from leader_deadline_preview import preview_content, send_once, validate_request
from tracker import DeliveryError, Tracker, VIETNAM


class LeaderPreviewChecks(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 24, 10, tzinfo=VIETNAM).timestamp()
        self.db = sqlite3.connect(':memory:')
        self.tracker = Tracker(self.db, {'leader_staff_id': 'synthetic-leader', 'leader_name': 'Leader thử nghiệm',
                                        'conversation_id': 'synthetic-group', 'robot_code': 'synthetic-bot'})

    def tearDown(self):
        self.db.close()

    def test_valid_request_is_fresh_and_cannot_select_another_recipient(self):
        request = {'request_id': '12345678-1234-1234-1234-123456789abc',
                   'requested_at': datetime.fromtimestamp(self.now, timezone.utc).isoformat(),
                   'source': 'leader-deadline-preview'}
        self.assertEqual(validate_request(request, self.now), request['request_id'])
        with self.assertRaises(StateError): validate_request({**request, 'target': 'another-person'}, self.now)
        with self.assertRaises(StateError): validate_request(request, self.now + 3601)

    def test_actual_pending_tasks_are_combined_without_creating_send_jobs(self):
        incoming = SimpleNamespace(sender_staff_id='synthetic-leader')
        for i, name in enumerate(('Nộp 2 video', 'Điền báo cáo')):
            self.tracker.save_task(name, self.now + 86400 + i * 3600, incoming, str(i), self.now - 100,
                                   ['synthetic-trainer', 'synthetic-leader'])
        content, count = preview_content(self.tracker, self.now)
        self.assertEqual(count, 2)
        self.assertIsInstance(content, MarkdownMessage)
        self.assertIn('1. Nộp 2 video', content)
        self.assertIn('2. Điền báo cáo', content)
        self.assertEqual(self.tracker.next_jobs(self.now), [])

    def test_no_active_deadline_is_stated_without_inventing_tasks(self):
        content, count = preview_content(self.tracker, self.now)
        self.assertEqual(count, 0)
        self.assertIn('không có công việc còn hạn', content)
        self.assertEqual(self.tracker.pending_tasks(), [])

    def test_only_one_dm_to_leader_and_same_request_does_not_send_twice(self):
        sender, store = Mock(), Mock()
        sender.send.return_value = 'synthetic-receipt'
        content = MarkdownMessage('Synthetic preview')
        result = send_once(self.db, self.tracker, sender, store, 'request', content, 2, self.now)
        self.assertEqual(result['accepted'], 1)
        sender.send.assert_called_once_with('dm', 'synthetic-leader', content)
        self.assertEqual(result['group_accepted'], 0)
        self.assertEqual(result['trainer_accepted'], 0)
        again = send_once(self.db, self.tracker, sender, store, 'request', content, 2, self.now)
        self.assertEqual(again['accepted'], 1)
        self.assertEqual(sender.send.call_count, 1)

    def test_unknown_send_is_never_retried(self):
        sender, store = Mock(), Mock()
        sender.send.side_effect = DeliveryError('timeout', ambiguous=True)
        first = send_once(self.db, self.tracker, sender, store, 'uncertain', 'Preview', 2, self.now)
        again = send_once(self.db, self.tracker, sender, store, 'uncertain', 'Preview', 2, self.now)
        self.assertEqual(first['uncertain'], 1)
        self.assertEqual(again['accepted'], 0)
        self.assertEqual(sender.send.call_count, 1)

    def test_failed_guard_save_prevents_any_send(self):
        sender, store = Mock(), Mock()
        store.save.side_effect = StateError('synthetic-write-failure')
        with self.assertRaises(StateError):
            send_once(self.db, self.tracker, sender, store, 'save-failed', 'Preview', 2, self.now)
        sender.send.assert_not_called()


if __name__ == '__main__': unittest.main()
