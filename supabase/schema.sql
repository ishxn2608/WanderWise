-- WanderWise — Supabase schema
-- Safe to run multiple times (idempotent).

create extension if not exists pgcrypto;

create table if not exists public.trips (
  id           uuid          primary key default gen_random_uuid(),
  user_id      uuid          not null references auth.users(id) on delete cascade,
  destination  text          not null check (char_length(destination) between 2 and 120),
  start_date   date          not null,
  end_date     date          not null,
  budget       numeric(14,2) not null check (budget > 0),
  currency     text          not null default 'INR' check (currency in ('INR','USD','EUR','GBP')),
  itinerary    jsonb         not null,
  created_at   timestamptz   not null default now(),
  constraint trips_dates_valid check (end_date >= start_date)
);

create index if not exists trips_user_created_idx
  on public.trips(user_id, created_at desc);

alter table public.trips enable row level security;

-- Drop existing policies before recreating (safe on re-run)
drop policy if exists "Users can view own trips"   on public.trips;
drop policy if exists "Users can create own trips" on public.trips;
drop policy if exists "Users can update own trips" on public.trips;
drop policy if exists "Users can delete own trips" on public.trips;

create policy "Users can view own trips"
  on public.trips for select
  to authenticated
  using (auth.uid() = user_id);

create policy "Users can create own trips"
  on public.trips for insert
  to authenticated
  with check (auth.uid() = user_id);

create policy "Users can update own trips"
  on public.trips for update
  to authenticated
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

create policy "Users can delete own trips"
  on public.trips for delete
  to authenticated
  using (auth.uid() = user_id);
