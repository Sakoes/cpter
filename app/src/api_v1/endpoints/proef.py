from http.client import HTTPException
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.crud import crud_proef
from app.schemas.proef import ProefCreate
from app import deps

proef_api = APIRouter(prefix="/proeven", tags=["proef"])

@proef_api.get("/", status_code=200)
def root(
    db: Session = Depends(deps.get_db),
    ) -> dict:
    
    """
    Root GET
    """
    proeven = crud_proef.proef.get_multi(db=db, limit=10)
    return {"proeven": proeven}

@proef_api.get("/proef/{id}", status_code=200)
def get_by_id(
    id: int,
    db: Session = Depends(deps.get_db),
    ) -> any:
    
    """
    Fetch a single proef by ID
    """
    result = crud_proef.proef.get(db=db, id=id)  # 2
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Proef with ID {id} not found"
        )

    return result

@proef_api.post("/post", status_code=200)
def post_proef(
    proef: ProefCreate, 
    db: Session = Depends(deps.get_db),
    ):
    
    """
    Add proef.
    """
    result = crud_proef.proef.create(db=db, obj_in=proef)
    return result