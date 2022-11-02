from pydantic import BaseModel
from dtw import *


class DtwInput(BaseModel):
    x: list[float]
    y: list[float]
    open_end: bool = False
    open_begin: bool = False
    distance_only: bool = False
    
class DtwOutput(BaseModel):
    distance: float = 0
    normalizedDistance: float = 0
    index1: list[int] = None
    index2: list[int] = None