from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.proef import Proef
from app.schemas.proef import ProefCreate, ProefUpdate


class CRUDProef(CRUDBase[Proef, ProefCreate, ProefUpdate]):
    def test_proef_CRUD(
        self, db: Session, *, obj_in: ProefCreate
    ) -> Proef:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


proef = CRUDProef(Proef)