"""
Backend API tests — run from the backend/ directory:
    pytest
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "demo_mode" in data


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_fallback_itinerary():
    response = client.post(
        "/api/itinerary",
        json={
            "destination": "Ujjain",
            "start_date": "2026-11-10",
            "end_date": "2026-11-11",
            "budget": 5000,
            "currency": "INR",
            "travelers": 2,
            "travel_style": "Balanced",
            "interests": ["Culture", "Food"],
            "accommodation": "Budget",
            "notes": "",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["days"]) == 2
    assert body["generated_by"] == "fallback"
    assert body["destination"] == "Ujjain"
    assert isinstance(body["total_estimated_cost"], (int, float))
    assert isinstance(body["transport_tips"], list)
    assert isinstance(body["practical_tips"], list)


def test_invalid_dates():
    response = client.post(
        "/api/itinerary",
        json={
            "destination": "Ujjain",
            "start_date": "2026-11-12",
            "end_date": "2026-11-10",
            "budget": 5000,
        },
    )
    assert response.status_code == 422


def test_missing_destination():
    response = client.post(
        "/api/itinerary",
        json={"start_date": "2026-11-10", "end_date": "2026-11-11", "budget": 5000},
    )
    assert response.status_code == 422


def test_single_day_trip():
    response = client.post(
        "/api/itinerary",
        json={
            "destination": "Delhi",
            "start_date": "2026-12-01",
            "end_date": "2026-12-01",
            "budget": 3000,
            "currency": "INR",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["days"]) == 1
    assert body["generated_by"] == "fallback"
