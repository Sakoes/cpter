import logging

from app.schemas.proef import ProefCreate
from app.crud import crud_proef
from app.db import base  # noqa: F401
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db() -> None:

    db = SessionLocal()
    
    if crud_proef.proef.get(db, 1) == None:
        proef_in = ProefCreate(
            description="Initial test object",
            xCor="1",
            yCor="2",
            zCor=3
        )
        crud_proef.proef.create(db, obj_in=proef_in)


def main() -> None:
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")

if __name__ == "__main__":
    main()
