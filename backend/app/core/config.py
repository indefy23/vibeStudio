import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./vibeestudio.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    STORAGE_PATH: str = "./projects"
    WHISPER_MODEL: str = "tiny"
    OPENROUTER_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure storage path exists
os.makedirs(settings.STORAGE_PATH, exist_ok=True)
