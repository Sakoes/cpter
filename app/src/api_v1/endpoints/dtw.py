'''
DTW docs -> https://dynamictimewarping.github.io/py-api/html/api/dtw.dtw.html#dtw.dtw
'''

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dtw import *
import json

from app.schemas.dtw import DtwInput, DtwOutput


dtw_api = APIRouter(prefix="/dtw", tags=["dtw"])

@dtw_api.post("/", response_model=DtwOutput)
def exec_dtw(input: DtwInput):
    alignment: DTW = dtw(x=input.x, y=input.y)
    return alignment
    """ json_compatible_item_data = jsonable_encoder(alignment)
    return JSONResponse(content=json_compatible_item_data) """


@dtw_api.post("/b")
def exec_dtw(input_x: list[float], input_y: list[float]):
    alignment = dtw.dtw(input_x, input_y)
    
    #return getattr(alignment, "distance")
     
    json_compatible_item_data = jsonable_encoder(alignment)
    return JSONResponse(content=json_compatible_item_data)