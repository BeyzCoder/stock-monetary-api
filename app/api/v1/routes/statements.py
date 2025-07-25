from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/income/{symbol}')
async def income(symbol):
    return JSONResponse(
        content={'symbol':symbol},
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )