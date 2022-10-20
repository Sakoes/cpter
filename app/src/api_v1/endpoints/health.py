from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_items():
    """
    Retrieve items.
    """
    return "This is the health endpoint"
