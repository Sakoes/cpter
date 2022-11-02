# https://testdriven.io/blog/fastapi-docker-traefik/
    
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base import Base

class Proef(Base):
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    xCor = Column(Float)
    yCor = Column(Float)
    zCor: Column(Float)
    #metingen = relationship("Meting", back_populates="proef")
    #tags: List[str]
    
    
""" class Meting(Base):
    id = Column(Integer, primary_key=True, index=True)
    proef = relationship("Proef", back_populates="metingen")
    conus = Column(float)
    kleef = Column(float)
    depth = Column(float)
 """
