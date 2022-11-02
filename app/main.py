from fastapi import FastAPI

from app.src.api_v1.api import api_router
from app.core.config import settings
from app.db.session import database
from app.models.proef import Proef

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await Proef.objects.get_or_create(description="test description")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()