from sqlalchemy.orm import Session

from app.crud import crud_proef
from app.schemas.proef import ProefCreate

def test_create_item(db: Session) -> None:
    proef_in = ProefCreate(description="test0711")
    proef = crud_proef.proef.test_proef_CRUD(db=db, obj_in=proef_in)
    assert proef.description == proef_in.description
