from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CPTER"
    API_V1_STR: str = "/api/v1"
    HEALTH_ENDPOINT: str = "/health"


settings = Settings()
