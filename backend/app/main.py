from __future__ import annotations

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .schemas import TripRequest, ItineraryResponse
from .planner import generate

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="AI-assisted personalized travel itinerary API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"name": settings.app_name, "status": "ok", "docs": "/docs"}


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "ai_configured": bool(settings.ai_api_key and settings.ai_model),
        "demo_mode": not bool(settings.ai_api_key and settings.ai_model),
        "model": settings.ai_model or "none",
        "base_url": settings.ai_base_url,
    }


@app.post("/api/itinerary", response_model=ItineraryResponse)
async def create_itinerary(request: TripRequest):
    try:
        return await generate(request, settings)
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AI provider returned HTTP {exc.response.status_code}; check API key, model and endpoint.",
        )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="AI provider timed out. Please retry.")
    except (KeyError, ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AI provider returned an invalid itinerary ({exc}). Please retry.",
        )
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Could not reach the AI provider.")
