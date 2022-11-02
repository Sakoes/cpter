from pydantic import BaseModel
from typing import List


class ProefInput(BaseModel):
    description: str
    xCor: str
    yCor: str
    z_para: float
    conus: List[float]
    kleef: List[float]
    time: List[float]
    depth: List[float]
    tags: List[str]
    
    
class ProefOutput(BaseModel):
    id: int
    description: str
    xCor: str
    yCor: str
    z_para: float
    conus: List[float]
    kleef: List[float]
    time: List[float]
    depth: List[float]
    tags: List[str]