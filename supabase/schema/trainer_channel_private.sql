create table public.trainer_channel_private (
  key text primary key,
  value jsonb not null,
  version integer not null default 1,
  updated_at timestamptz not null default now()
);
alter table public.trainer_channel_private enable row level security;
revoke all on public.trainer_channel_private from public, anon, authenticated;
grant all on public.trainer_channel_private to service_role;
comment on table public.trainer_channel_private is 'Trainer TikTok connections, OAuth state and private metrics. Edge Function only; encrypted payloads; no public policies.';
