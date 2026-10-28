# WanderWise API Reference

Base URL (local): `http://localhost:8001`  
Base URL (production): `https://wanderwise-api.onrender.com`

Interactive docs: `{base_url}/docs`

---

## GET /api/health

Returns the API status and AI configuration state.

**Response**
```json
{
  "status": "healthy",
  "ai_configured": true,
  "demo_mode": false,
  "model": "qwen/qwen3.8-27b",
  "base_url": "https://api.groq.com/openai/v1"
}
```

---

## POST /api/itinerary

Generates a personalized day-by-day travel itinerary.

**Request Body**
```json
{
  "destination": "Ujjain, Madhya Pradesh",
  "start_date": "2026-11-10",
  "end_date": "2026-11-12",
  "budget": 8000,
  "currency": "INR",
  "travelers": 2,
  "travel_style": "Balanced",
  "interests": ["Culture", "Spirituality", "Food"],
  "accommodation": "Budget",
  "notes": "Include Mahakaleshwar temple"
}
```

**Fields**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `destination` | string | ✅ | City, region or country (2–120 chars) |
| `start_date` | date | ✅ | YYYY-MM-DD |
| `end_date` | date | ✅ | YYYY-MM-DD, must be ≥ start_date |
| `budget` | number | ✅ | Total trip budget (> 0) |
| `currency` | string | | INR / USD / EUR / GBP (default: INR) |
| `travelers` | integer | | 1–30 (default: 1) |
| `travel_style` | string | | Relaxed / Balanced / Packed |
| `interests` | array | | Up to 12 interest tags |
| `accommodation` | string | | Budget / Mid-range / Luxury / Not needed |
| `notes` | string | | Free text up to 1000 chars |

**Response**
```json
{
  "destination": "Ujjain, Madhya Pradesh",
  "summary": "A 3-day balanced plan...",
  "currency": "INR",
  "total_estimated_cost": 4200,
  "budget_remaining": 3800,
  "budget_note": "Illustrative estimates only.",
  "transport_tips": ["..."],
  "practical_tips": ["..."],
  "days": [
    {
      "day": 1,
      "date": "2026-11-10",
      "title": "Day 1: Arrive in Ujjain",
      "morning": [
        {
          "time": "09:00",
          "title": "Mahakaleshwar Temple",
          "description": "Visit the sacred Jyotirlinga...",
          "estimated_cost": 50,
          "category": "Spirituality"
        }
      ],
      "afternoon": [],
      "evening": []
    }
  ],
  "generated_by": "ai"
}
```

**Error Responses**

| Code | Meaning |
|------|---------|
| 422 | Validation error (bad dates, missing fields) |
| 502 | AI provider error |
| 504 | AI provider timeout |
