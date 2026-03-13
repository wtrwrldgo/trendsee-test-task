from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://trendsee:trendsee_pass@localhost:5432/trendsee"
    redis_url: str = "redis://localhost:6379"
    jwt_secret: str = "super-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24

    class Config:
        env_file = ".env"


settings = Settings()
