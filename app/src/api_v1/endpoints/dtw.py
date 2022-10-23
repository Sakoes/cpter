'''
DTW docs -> https://dynamictimewarping.github.io/py-api/html/api/dtw.dtw.html#dtw.dtw
'''

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.dtw import DtwInput
import dtw

dtw_api = APIRouter(prefix="/dtw", tags=["dtw"])

@dtw_api.post("/")
def exec_dtw(input: DtwInput):
    alignment = dtw.dtw(x=input.x, y=input.y, open_begin=input.open_end, open_end=input.open_end)
    
    json_compatible_item_data = jsonable_encoder(alignment)
    return JSONResponse(content=json_compatible_item_data)