from unittest.mock import Base
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Loads and validates app config from .env or environment variables."""

    # Allowed origins for CORS (Cross-Origin Resource Sharing)
    # Frontend dev server runs on port 5174 (Vite default)
    backend_cors_origins: list[str] = [
        "http://localhost:5174",
        "http://127.0.0.1:5174"
        ]  

    # App metadata
    app_name: str = "MoneyMind"
    debug: bool = False  # Enable for verbose logging

    # Database connection string (loaded from DATABASE_URL)
    database_url: str

    # JWT token settings (loaded from JWT_SECRET_KEY)
    jwt_secret_key: str  # Used to sign/verify tokens
    jwt_algorithm: str = "HS256"  # Signing algorithm
    access_token_expire_minutes: int = 30  # Token validity duration

    
    model_config = SettingsConfigDict(
        env_file=".env",  # Load vars from this file
        case_sensitive=False,  # DATABASE_URL == database_url
        extra="ignore"  # Ignore unknown env vars
    )
        
# Instantiated once, import this in other modules
settings = Settings()
    
print("Loaded settings from environment variables.")