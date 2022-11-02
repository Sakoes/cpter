from fastapi import APIRouter

proef_api = APIRouter(prefix="/proef", tags=["proef"])

@proef_api.get("/")
def get_proef():
    """
    Retrieve items.
    """
    return {"This is the health endpoint"}