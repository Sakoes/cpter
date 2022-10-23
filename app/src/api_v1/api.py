from fastapi import APIRouter

from app.src.api_v1.endpoints import health, test, dtw

api_router = APIRouter()
api_router.include_router(health.health_api)
api_router.include_router(test.test_api)
api_router.include_router(dtw.dtw_api)