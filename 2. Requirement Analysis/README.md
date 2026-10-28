# Phase 2: Requirement Analysis

## Functional Requirements

| # | Requirement | Status |
|---|-------------|--------|
| 1 | Trip form: destination, dates, budget, currency, travelers | ✅ |
| 2 | Travel style and interests selection | ✅ |
| 3 | AI itinerary generation via Groq API | ✅ |
| 4 | Demo fallback when no AI key configured | ✅ |
| 5 | Day-by-day plan with morning/afternoon/evening slots | ✅ |
| 6 | Cost estimates and budget remaining | ✅ |
| 7 | Transport tips and practical travel tips | ✅ |
| 8 | Save trip to Supabase (authenticated) | ✅ |
| 9 | Save trip to localStorage (guest) | ✅ |
| 10 | Email/password authentication via Supabase | ✅ |
| 11 | Print / Save as PDF | ✅ |

## Non-Functional Requirements

- Response time < 30s for AI generation
- Works on mobile and desktop (responsive)
- No API keys required for demo mode
- Row Level Security on all database queries
- CORS locked to known frontend origins

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, Vite 6, Lucide Icons |
| Backend | FastAPI, Python 3.8+, Pydantic v2 |
| AI Provider | Groq (qwen/qwen3.8-27b) |
| Database | Supabase (PostgreSQL) |
| Auth | Supabase Auth (email/password) |
| Hosting | Vercel (frontend), Render (backend) |

## Data Flow

```
User Input → React Form → POST /api/itinerary → FastAPI → Groq API → JSON Response → React UI → Supabase/localStorage
```
