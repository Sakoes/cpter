from http.client import HTTPException
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.crud import crud_proef
from app.schemas.proef import ProefCreate, ProefDB
from app.models.proef import Proef
from app.src import deps

proef_api_v2 = SQLAlchemyCRUDRouter(
    schema=ProefDB,
    create_schema=ProefCreate,
    db_model=Proef,
    db=deps.get_db,
    prefix='proef_v2'
)