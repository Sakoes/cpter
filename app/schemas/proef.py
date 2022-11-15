from pydantic import BaseModel
from typing import List

class ProefBase(BaseModel):
    description: str
    xCor: float
    yCor: float
    zCor: float

class ProefCreate(ProefBase):
    description: str
    xCor: float
    yCor: float
    zCor: float
    """ conus: List[float]
    kleef: List[float]
    time: List[float]
    depth: List[float]
    tags: List[str] """
    
class ProefUpdate(ProefBase):
    description: str
    
class ProefDB(ProefBase):
    id: int
    description: str
    xCor: float
    yCor: float
    zCor: float
    
    class Config:
        orm_mode = True
        
class ProefOutput(ProefBase):
    pass