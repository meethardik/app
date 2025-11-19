from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "gpt-4"
    temperature: float = 0.0

    class Config:
        env_file = ".env"

settings = Settings()