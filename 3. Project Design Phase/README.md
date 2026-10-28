# Phase 3: Project Design Phase

## Solution Architecture

```
┌─────────────────────────────┐
│   Vercel (Frontend)         │
│   React + Vite              │
│   wanderwise-henna.vercel   │
└──────────────┬──────────────┘
               │ HTTPS POST /api/itinerary
               ▼
┌─────────────────────────────┐
│   Render (Backend)          │
│   FastAPI + Uvicorn         │
│   wanderwise-api.onrender   │
└──────┬──────────────┬───────┘
       │              │
       ▼              ▼
┌──────────┐   ┌──────────────┐
│ Groq API │   │  Supabase    │
│ (AI LLM) │   │  (Auth + DB) │
└──────────┘   └──────────────┘
```

## Database Schema

See `Database Schema/` folder for full SQL.

**trips table:**
- `id` — UUID primary key
- `user_id` — FK to auth.users (RLS enforced)
- `destination`, `start_date`, `end_date`, `budget`, `currency`
- `itinerary` — JSONB (full AI response stored)
- `created_at` — timestamp

## UI Design Decisions

- Single-page app with 3 tabs: Plan / Itinerary / Saved
- Collapsible day cards to reduce cognitive load
- Chip-based interest selector for quick multi-select
- Print-friendly CSS for PDF export
- Status indicator: "API connected" vs "Demo mode"
