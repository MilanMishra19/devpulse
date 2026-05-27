from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str = ""
    GITHUB_WEBHOOK_SECRET: str = "dev_secret"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/flowguard"
    TIMESCALE_URL: str = "postgresql://postgres:postgres@localhost:5433/flowguard_metrics"
    REDIS_URL: str = "redis://localhost:6379"
    SLACK_WEBHOOK_URL: str = ""
    CLASSIFIER_CONFIDENCE_THRESHOLD: float = 0.7
    CORRELATION_BLAME_WINDOW_SECONDS: int = 300

    class Config:
        env_file = ".env"

settings = Settings()