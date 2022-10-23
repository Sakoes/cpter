from fastapi import APIRouter

test_api = APIRouter(prefix="/test", tags=["test"])

@test_api.get("/")
def get_test():
    """
    Retrieve items.
    """
    return {"This is the test endpoint"}

@test_api.post("/post_var_test")
def post_var(input):
    return input

@test_api.post("/post_array_test")
def post_array(input: list[float]):
    return input