from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse 

from app.api.v1.routes import route_statements

app = FastAPI()
# routers connected.
app.include_router(route_statements.router, prefix="/api/v1/statements")


@app.get('/')
async def root():
    return JSONResponse(
        content={'status':"Server up running!"},
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)  # No Content