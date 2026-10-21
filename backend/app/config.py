from __future__ import annotations

from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

# Always resolve .env relative to this file's directory (backend/app/../.env = backend/.env)
_ENV_FILE = Path(__file__).parent.parent / ".env"


class Settings(BaseSettings):
    app_name: str = "Personalized Travel Itinerary Planner API"
    environment: str = "development"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    ai_api_key: str = ""
    ai_base_url: str = "https://api.openai.com/v1"
    ai_model: str = ""
    model_config = SettingsConfigDict(env_file=str(_ENV_FILE), extra="ignore")

    @property
    def origin_list(self) -> list[str]:
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
