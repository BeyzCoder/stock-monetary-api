from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import Depends

from app.api.v1.db.database import get_db
from app.api.v1.db.retrieve_facts import get_facts
from app.api.v1.schemas.schema_statements import StatementTypeSchema

router = APIRouter()


@router.get('/income/{symbol}')
async def income(symbol, db: Session = Depends(get_db)):
    facts = get_facts(symbol, "Income", db)
    deconstructed = StatementTypeSchema.from_statement(facts)
    return JSONResponse(
        content=deconstructed.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )


@router.get('/balance/{symbol}')
async def balance(symbol, db: Session = Depends(get_db)):
    facts = get_facts(symbol, "Balance", db)
    deconstructed = StatementTypeSchema.from_statement(facts)
    return JSONResponse(
        content=deconstructed.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )


@router.get('/cash/{symbol}')
async def cash(symbol, db: Session = Depends(get_db)):
    facts = get_facts(symbol, "Cash", db)
    deconstructed = StatementTypeSchema.from_statement(facts)
    return JSONResponse(
        content=deconstructed.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )