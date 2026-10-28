# WanderWise — Local Setup Guide

## Prerequisites

- Python 3.8+
- Node.js 18+
- Git

---

## Backend Setup

```powershell
# 1. Navigate to backend
Set-Location backend

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create environment file
Copy-Item .env.example .env
# Edit .env and add your Groq API key (optional for demo mode)

# 5. Start the server
uvicorn app.main:app --reload --port 8001
```

API available at: http://localhost:8001  
Docs available at: http://localhost:8001/docs

---

## Frontend Setup

```powershell
# 1. Navigate to frontend
Set-Location frontend

# 2. Install dependencies
npm install

# 3. Create environment file
Copy-Item .env.example .env
# Edit .env — set VITE_API_BASE_URL=http://localhost:8001

# 4. Start dev server
npm run dev
```

App available at: http://localhost:5173

---

## Optional: Supabase Setup

1. Create project at https://supabase.com
2. Run `supabase/schema.sql` in SQL Editor
3. Go to Authentication → Sign In / Providers → disable "Confirm email"
4. Copy Project URL and anon key into `frontend/.env`

---

## Demo Mode

Works without any API keys. Leave `AI_API_KEY` and `AI_MODEL` blank in `backend/.env` to use the built-in fallback itinerary generator.

---

## Run Tests

```powershell
Set-Location backend
.\.venv\Scripts\Activate.ps1
pytest -v
```

Expected: 6 tests pass.
