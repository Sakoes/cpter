from fastapi import APIRouter

#from authx import Authentication, BaseDBBackend, RedisBackend, User

from app.src.api_v1.endpoints import health, test, dtw, proef, proef_v2

api_router = APIRouter()
api_router.include_router(health.health_api)
#api_router.include_router(test.test_api)
#api_router.include_router(dtw.dtw_api)
api_router.include_router(proef.proef_api)
api_router.include_router(proef_v2.proef_api_v2)


""" auth = Authentication(database_backend=BaseDBBackend())
api_router.include_router(auth.auth_router, prefix="/api/users")
api_router.include_router(auth.social_router, prefix="/auth")
api_router.include_router(auth.password_router, prefix="/api/users")
api_router.include_router(auth.admin_router, prefix="/api/users")
api_router.include_router(auth.search_router, prefix="/api/users") """