from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent


# Authentication JWT Settings
class AuthJWT(BaseSettings):
    private_key: Path = BASE_DIR / "certs/private.pem"
    public_key: Path = BASE_DIR / "certs/public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


# Main Settings
class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db") # Default to SQLite for simplicity. Change in production.

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    AUTH_JWT: AuthJWT = AuthJWT()

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore",
    }


# Cached settings instance
@lru_cache()
def get_settings() -> Settings:
    return Settings()
