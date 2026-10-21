from __future__ import annotations

from datetime import date
from typing import List, Literal
from pydantic import BaseModel, Field, model_validator


class TripRequest(BaseModel):
    destination: str = Field(min_length=2, max_length=120)
    start_date: date
    end_date: date
    budget: float = Field(gt=0, le=100_000_000)
    currency: Literal["INR", "USD", "EUR", "GBP"] = "INR"
    travelers: int = Field(default=1, ge=1, le=30)
    travel_style: Literal["Relaxed", "Balanced", "Packed"] = "Balanced"
    interests: List[str] = Field(default_factory=list, max_length=12)
    accommodation: Literal["Budget", "Mid-range", "Luxury", "Not needed"] = "Mid-range"
    notes: str = Field(default="", max_length=1000)

    @model_validator(mode="after")
    def check_dates(self) -> TripRequest:
        if self.end_date < self.start_date:
            raise ValueError("End date must be on or after start date.")
        if (self.end_date - self.start_date).days > 30:
            raise ValueError("Trips longer than 31 calendar days are not supported.")
        return self


class Activity(BaseModel):
    time: str
    title: str
    description: str
    estimated_cost: float = Field(ge=0)
    category: str = "Activity"


class ItineraryDay(BaseModel):
    day: int
    date: str
    title: str
    morning: List[Activity] = Field(default_factory=list)
    afternoon: List[Activity] = Field(default_factory=list)
    evening: List[Activity] = Field(default_factory=list)


class ItineraryResponse(BaseModel):
    destination: str
    summary: str
    currency: str
    total_estimated_cost: float
    budget_remaining: float
    budget_note: str
    transport_tips: List[str]
    practical_tips: List[str]
    days: List[ItineraryDay]
    generated_by: str = "fallback"
