'''
DTW docs -> https://dynamictimewarping.github.io/py-api/html/api/dtw.dtw.html#dtw.dtw
'''

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import dtw

from app.schemas.dtw import DtwInput


dtw_api = APIRouter(prefix="/dtw", tags=["dtw"])

@dtw_api.post("/a")
def exec_dtw(input: DtwInput):
    alignment = dtw.dtw(x=input.x, y=input.y, open_begin=input.open_end, open_end=input.open_end)
    
    json_compatible_item_data = jsonable_encoder(alignment)
    return JSONResponse(content=json_compatible_item_data)


@dtw_api.post("/b")
def exec_dtw(input_x: list[float], input_y: list[float]):
    alignment = dtw.dtw(input_x, input_y)
    
    #return getattr(alignment, "distance")
     
    json_compatible_item_data = jsonable_encoder(alignment)
    return JSONResponse(content=json_compatible_item_data)