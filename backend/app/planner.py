from __future__ import annotations

import json
from datetime import timedelta
import httpx
from .schemas import TripRequest, ItineraryResponse

SYSTEM_PROMPT = (
    "You are a careful travel planner. Always respond with a single valid json object and nothing else. "
    "The json must have exactly these keys: "
    "destination (string), summary (string), currency (string), total_estimated_cost (number), "
    "budget_remaining (number), budget_note (string), "
    "transport_tips (array of strings), practical_tips (array of strings), days (array). "
    "Each day object has: day (int), date (YYYY-MM-DD string), title (string), "
    "morning (array), afternoon (array), evening (array). "
    "Each activity object has: time (HH:MM string), title (string), description (string), "
    "estimated_cost (number >= 0), category (string). "
    "Keep estimates within budget when practical. Do not claim live availability or exact current prices. "
    "Clearly label prices as estimates. Output raw json only — no markdown, no code fences."
)


def fallback(req: TripRequest) -> ItineraryResponse:
    count = (req.end_date - req.start_date).days + 1
    templates = [
        ("09:00", "Explore a local landmark", "Visit a popular heritage or cultural attraction; verify opening times.", "Sightseeing", 300),
        ("13:00", "Try regional food", "Choose a local restaurant and pair lunch with a nearby attraction.", "Food & culture", 450),
        ("17:30", "Enjoy a market or scenic walk", "Keep the evening flexible and plan safe transport back.", "Leisure", 250),
    ]
    days = []
    for n in range(count):
        d = req.start_date + timedelta(days=n)
        periods = []
        for time, title, desc, category, base_cost in templates:
            cost = round(min(base_cost, req.budget / count * 0.35), 2)
            periods.append({
                "time": time,
                "title": title,
                "description": f"{desc} Adapt this suggestion for {req.destination}.",
                "estimated_cost": cost,
                "category": category,
            })
        days.append({
            "day": n + 1,
            "date": d.isoformat(),
            "title": f"Day {n + 1}: Discover {req.destination}",
            "morning": [periods[0]],
            "afternoon": [periods[1]],
            "evening": [periods[2]],
        })
    total = round(
        sum(
            a["estimated_cost"]
            for day in days
            for period_key in ("morning", "afternoon", "evening")
            for a in day[period_key]
        ),
        2,
    )
    return ItineraryResponse(
        destination=req.destination,
        summary=(
            f"A {count}-day {req.travel_style.lower()} starter plan for {req.travelers} traveler(s). "
            f"Interests: {', '.join(req.interests) or 'local highlights'}. "
            "This demo uses generic suggestions; replace them with verified local options."
        ),
        currency=req.currency,
        total_estimated_cost=total,
        budget_remaining=round(max(0.0, req.budget - total), 2),
        budget_note=(
            "Illustrative activity estimates only; may exclude accommodation, "
            "flights, taxes and ticket changes."
        ),
        transport_tips=[
            "Group nearby attractions to reduce transfers.",
            "Check local transit schedules and fares.",
            "Use licensed transport and confirm your route.",
        ],
        practical_tips=[
            "Check official attraction sites for opening hours and ticket rules.",
            "Leave time for weather, queues and rest.",
            "Verify safety guidance and bookings before travel.",
        ],
        days=days,
        generated_by="fallback",
    )


async def generate(req: TripRequest, settings) -> ItineraryResponse:
    if not settings.ai_api_key or not settings.ai_model:
        return fallback(req)

    payload = {
        "model": settings.ai_model,
        "temperature": 0.4,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": "Return a json travel itinerary for this request: "
                + json.dumps(req.model_dump(mode="json")),
            },
        ],
    }
    async with httpx.AsyncClient(timeout=45) as client:
        response = await client.post(
            settings.ai_base_url.rstrip("/") + "/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.ai_api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
        )
        response.raise_for_status()
        body = response.json()

    data = json.loads(body["choices"][0]["message"]["content"])
    data["generated_by"] = "ai"
    result = ItineraryResponse.model_validate(data)
    result.destination = req.destination
    result.budget_remaining = round(max(0.0, req.budget - result.total_estimated_cost), 2)
    if result.total_estimated_cost > req.budget:
        result.budget_note = (
            "Generated estimates exceed your budget; revise the plan before relying on it."
        )
    return result
