# WanderWise — Deployment Guide

## Live URLs

| Service | URL |
|---------|-----|
| Frontend | https://wanderwise-henna.vercel.app |
| Backend API | https://wanderwise-api.onrender.com |
| API Health | https://wanderwise-api.onrender.com/api/health |
| API Docs | https://wanderwise-api.onrender.com/docs |

---

## Backend — Render

**Service type:** Web Service  
**Runtime:** Python 3  
**Root Directory:** `backend`  
**Build Command:** `pip install -r requirements.txt`  
**Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`  
**Health Check:** `/api/health`

### Environment Variables on Render

| Key | Value |
|-----|-------|
| `AI_API_KEY` | Groq API key |
| `AI_BASE_URL` | https://api.groq.com/openai/v1 |
| `AI_MODEL` | qwen/qwen3.8-27b |
| `CORS_ORIGINS` | https://wanderwise-henna.vercel.app |
| `ENVIRONMENT` | production |

---

## Frontend — Vercel

**Framework:** Vite  
**Root Directory:** `frontend`  
**Build Command:** `npx vite build`  
**Output Directory:** `dist`  
**Install Command:** `npm install`

### Environment Variables on Vercel

| Key | Value |
|-----|-------|
| `VITE_API_BASE_URL` | https://wanderwise-api.onrender.com |
| `VITE_SUPABASE_URL` | https://dykejuhawpmduhkhackd.supabase.co |
| `VITE_SUPABASE_ANON_KEY` | your anon key |

---

## Deployment Steps

1. Push code to `main` branch on GitHub
2. Render auto-deploys backend on push
3. Vercel auto-deploys frontend on push
4. Update `CORS_ORIGINS` on Render if Vercel URL changes

> **Note:** Render free tier sleeps after 15 minutes of inactivity. First request may take ~30 seconds.
