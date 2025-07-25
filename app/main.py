from fastapi import FastAPI, status
from fastapi.responses import JSONResponse 

from api.v1.routes import statements

app = FastAPI()
# routers connected.
app.include_router(statements.router, prefix="/api/v1/statements")


@app.get('/')
async def root():
    return JSONResponse(
        content={'status':"Server up running!"},
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )
