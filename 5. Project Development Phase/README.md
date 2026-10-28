# Phase 5: Project Development Phase

## Code Structure

```
WanderWise/
├── backend/
│   ├── app/
│   │   ├── main.py        FastAPI app, CORS, routes
│   │   ├── config.py      Settings via pydantic-settings
│   │   ├── schemas.py     Pydantic request/response models
│   │   ├── planner.py     AI call + demo fallback
│   │   └── __init__.py
│   ├── tests/
│   │   └── test_api.py    6 pytest tests (all pass)
│   ├── requirements.txt
│   ├── pytest.ini
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx        Main UI component
│   │   ├── lib/
│   │   │   ├── api.js     Backend fetch wrapper
│   │   │   └── supabase.js Supabase client
│   │   ├── main.jsx       React entry point
│   │   └── styles.css     Full responsive CSS
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js     Dev proxy to :8001
│   └── vercel.json
└── supabase/
    └── schema.sql
```

## Key Development Decisions

- **Python 3.8 compatibility:** Used `from __future__ import annotations` and `List[str]` instead of `list[str]`
- **Demo mode:** `planner.py` checks if `AI_API_KEY` is set; falls back to template-based generation
- **Groq JSON mode:** System prompt must contain lowercase "json" — Groq API requirement
- **CORS:** Configured via env var `CORS_ORIGINS` so both local and production origins work
- **Vite proxy:** Dev server proxies `/api/*` to backend, eliminating CORS issues locally

## Features Implemented

| Feature | File | Notes |
|---------|------|-------|
| Trip form | App.jsx | 9 input fields |
| AI itinerary | planner.py | Groq qwen3.8-27b |
| Demo fallback | planner.py | Template-based, no API needed |
| Supabase auth | App.jsx + supabase.js | Email/password |
| localStorage save | App.jsx | Guest mode fallback |
| Print to PDF | App.jsx | CSS @media print |
| Health endpoint | main.py | Shows AI status |
| 6 backend tests | test_api.py | All passing |
