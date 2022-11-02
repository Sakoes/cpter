from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "CPTER"
    API_V1_STR: str = "/api/v1"
    HEALTH_ENDPOINT: str = "/health"
    
    DB_URL: str = Field(..., env='DATABASE_URL')


settings = Settings()
