from pydantic import BaseSettings
from dotenv import load_dotenv, dotenv_values
import os

class Settings(BaseSettings):
    
    # Load environment variables from C:/Users/isaac/Desktop/python/cpter/app/.env
    #load_dotenv("./.env")
    load_dotenv()
    
    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "test")
    DB_URL: str = os.environ.get("DB_URL")
    API_V1_STR: str = os.environ.get("API_V1_STR", "/api/v1")
    HEALTH_ENDPOINT: str = os.environ.get("HEALTH_ENDPOINT")


settings = Settings()
