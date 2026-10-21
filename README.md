# WanderWise — Personalized Travel Itinerary Planner

A full-stack MVP using React + Vite (frontend) and Python FastAPI (backend).  
Works fully in **demo mode with no API keys required**.

## Features
- Responsive trip-planning form: destination, dates, budget, currency, travelers, pace, interests, accommodation, notes.
- Day-by-day itinerary with morning / afternoon / evening activities.
- Budget estimate, budget remaining, transport tips, and practical travel notes.
- **Demo fallback** — generates a complete itinerary without any AI key.
- Optional AI generation via any OpenAI-compatible `/chat/completions` endpoint.
- Supabase email/password auth and cloud trip saving when configured; local `localStorage` otherwise.
- Vite dev-proxy eliminates CORS issues during local development.
- FastAPI health endpoint (`/api/health`), interactive docs (`/docs`), validation, and 6 passing tests.
- SQL schema with Row Level Security, deployment templates for Render + Vercel.

---

## Run locally (Windows PowerShell)

### 1 — Backend

```powershell
Set-Location "backend"

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn app.main:app --reload
```

API runs at **http://localhost:8000**  
Interactive docs: **http://localhost:8000/docs**  
Health check: **http://localhost:8000/api/health**

### 2 — Frontend (separate PowerShell window)

```powershell
Set-Location "frontend"
npm install
npm run dev
```

App runs at **http://localhost:5173**

### 3 — Run backend tests

```powershell
Set-Location "backend"
.\.venv\Scripts\Activate.ps1
pytest -v
```

### 4 — Production build

```powershell
Set-Location "frontend"
npm run build          # output goes to frontend/dist/
```

---

## Configuration

### Backend — `backend/.env`
Copy `backend/.env.example` to `backend/.env`.  
Leave `AI_API_KEY` and `AI_MODEL` blank to use demo mode.

```
APP_NAME=Personalized Travel Itinerary Planner API
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
AI_API_KEY=            # optional — leave blank for demo mode
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL=              # e.g. gpt-4o-mini
```

### Frontend — `frontend/.env`
Copy `frontend/.env.example` to `frontend/.env`.  
Leave Supabase variables blank to use localStorage-only mode.

```
VITE_API_BASE_URL=http://localhost:8000
VITE_SUPABASE_URL=       # optional
VITE_SUPABASE_ANON_KEY=  # optional
```

---

## External setup still required

| Service | What to do | Required? |
|---------|-----------|-----------|
| **AI provider** | Set `AI_API_KEY`, `AI_MODEL`, `AI_BASE_URL` in `backend/.env`. Any OpenAI-compatible endpoint works (OpenAI, Azure OpenAI, Together, Groq, etc.). | Optional — demo mode works without it |
| **Supabase** | 1. Create a project at https://supabase.com. 2. Run `supabase/schema.sql` in the SQL Editor. 3. Enable Email auth. 4. Add project URL + anon key to `frontend/.env`. | Optional — localStorage saving works without it |
| **Deployment (backend)** | Deploy `backend/` to Render using `render.yaml`. Set `CORS_ORIGINS` to your Vercel frontend URL. | For production only |
| **Deployment (frontend)** | Deploy `frontend/` to Vercel. Set `VITE_API_BASE_URL` to your Render backend URL. | For production only |

> **Never commit real API keys.** Both `.env` files are in `.gitignore`.  
> Only the public Supabase **anon key** goes in the frontend — never the service-role key.  
> All prices and itinerary content are estimates; verify before travelling.

---

## Project structure

```
backend/
  app/
    main.py          FastAPI app, CORS, routes
    config.py        pydantic-settings, .env loading
    schemas.py       Request/response Pydantic models
    planner.py       Demo fallback + AI generation
    __init__.py
  tests/
    test_api.py      6 pytest tests (all pass)
  requirements.txt
  pytest.ini
  .env.example
  render.yaml        Render deployment config

frontend/
  src/
    App.jsx          Full React UI
    lib/api.js       Fetch wrapper for backend
    lib/supabase.js  Supabase client (null-safe)
    styles.css       Complete responsive CSS
  index.html
  vite.config.js     Dev proxy to :8000
  package.json
  .env.example
  vercel.json        Vercel SPA rewrite

supabase/
  schema.sql         Trips table + RLS policies
```
