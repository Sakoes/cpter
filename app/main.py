from fastapi import FastAPI

from app.src.api_v1.api import api_router
from app.core.config import settings
#from app.db.session import database

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

# DB tutorial
# https://testdriven.io/blog/fastapi-docker-traefik/

@app.on_event("startup")
async def startup():
    pass
    #if not database.is_connected:
        #await database.connect()
    # create a dummy entry
    #proef_in = ProefInput(description="test0711", xCor="5", yCor="6", zCor=7)
    #proef = crud_proef.proef.test_proef_CRUD(db=database, obj_in=proef_in)
    
    


@app.on_event("shutdown")
async def shutdown():
    pass
    #if database.is_connected:
        #await database.disconnect()