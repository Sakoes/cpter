from fastapi import APIRouter

from app.src.api_v1.endpoints import health, test, dtw, proef

api_router = APIRouter()
api_router.include_router(health.health_api)
api_router.include_router(test.test_api)
api_router.include_router(dtw.dtw_api)
api_router.include_router(proef.proef_api)