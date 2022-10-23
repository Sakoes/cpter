from pydantic import BaseModel

class DtwInput(BaseModel):
    x: list[float]
    y: list[float]
    open_end: bool = False
    open_begin: bool = False
    distance_only: bool = False