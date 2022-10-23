from fastapi import APIRouter

health_api = APIRouter(prefix="/health", tags=["health"])

@health_api.get("/")
def get_health():
    """
    Retrieve items.
    """
    return {"This is the health endpoint"}
