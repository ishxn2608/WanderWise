# WanderWise — System Architecture

## Overview

WanderWise is a full-stack travel itinerary planning application with three layers:

```
Browser (React + Vite)
        ↓  HTTPS
FastAPI Backend (Python)
        ↓  HTTPS
Groq AI API (LLM)
        +
Supabase (Auth + Database)
```

---

## Frontend (React + Vite)

- **Framework:** React 18 with Vite 6
- **Hosting:** Vercel
- **Key files:**
  - `src/App.jsx` — single-page UI (planner, itinerary, saved trips)
  - `src/lib/api.js` — fetch wrapper for backend calls
  - `src/lib/supabase.js` — Supabase client (null-safe when unconfigured)
  - `src/styles.css` — full responsive CSS

### Data flow (frontend)
1. User fills trip form → clicks "Generate"
2. `api.js` sends POST to `/api/itinerary`
3. Response rendered as day-by-day cards
4. User can save to Supabase (signed in) or localStorage (guest)

---

## Backend (FastAPI + Python)

- **Framework:** FastAPI 0.115+
- **Server:** Uvicorn
- **Hosting:** Render
- **Key files:**
  - `app/main.py` — routes, CORS middleware
  - `app/config.py` — pydantic-settings, .env loading
  - `app/schemas.py` — Pydantic request/response models
  - `app/planner.py` — AI call + demo fallback logic

### AI Generation flow
1. If `AI_API_KEY` + `AI_MODEL` are set → call Groq `/chat/completions`
2. If not set → return demo fallback itinerary
3. Response validated against `ItineraryResponse` schema

---

## Database (Supabase / PostgreSQL)

- **Table:** `public.trips`
- **Auth:** Supabase email/password
- **Security:** Row Level Security (RLS) — users can only see their own trips

```
trips
├── id (uuid, PK)
├── user_id (uuid, FK → auth.users)
├── destination (text)
├── start_date (date)
├── end_date (date)
├── budget (numeric)
├── currency (text)
├── itinerary (jsonb)
└── created_at (timestamptz)
```

---

## CORS Configuration

| Environment | Allowed Origins |
|------------|-----------------|
| Local dev | http://localhost:5173, http://127.0.0.1:5173 |
| Production | https://wanderwise-henna.vercel.app |

---

## Environment Variables

### Backend (`backend/.env`)
| Key | Purpose |
|-----|---------|
| `AI_API_KEY` | Groq API key |
| `AI_BASE_URL` | https://api.groq.com/openai/v1 |
| `AI_MODEL` | qwen/qwen3.8-27b |
| `CORS_ORIGINS` | Comma-separated allowed frontend origins |

### Frontend (`frontend/.env`)
| Key | Purpose |
|-----|---------|
| `VITE_API_BASE_URL` | Backend URL |
| `VITE_SUPABASE_URL` | Supabase project URL |
| `VITE_SUPABASE_ANON_KEY` | Supabase public anon key |
