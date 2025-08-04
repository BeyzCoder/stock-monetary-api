from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import Depends

from app.api.v1.db.database import get_db
from app.api.v1.db.retrieve_facts import get_facts
from app.api.v1.schemas.schema_statements import CompanyFactsSchema

from collections import defaultdict

def build_facts_schema(facts):
    nested_data = defaultdict(lambda: defaultdict(dict))

    for fact in facts:
        nested_data[fact.statement_type][fact.key_factor][fact.date] = float(fact.value)

    return CompanyFactsSchema.parse_obj(nested_data)

from datetime import date

def deconstruct_facts_schema(data):
    if isinstance(data, dict):
        # For dicts, process keys and values recursively
        new_dict = {}
        for k, v in data.items():
            # Convert date keys to string, else lowercase strings (optional)
            if isinstance(k, date):
                key_str = k.isoformat()
            else:
                # if keys like 'Income', you can make lowercase
                key_str = str(k).lower()
            new_dict[key_str] = deconstruct_facts_schema(v)
        return new_dict

    # For Pydantic model with `root` attribute (your data structure)
    if hasattr(data, "root"):
        return deconstruct_facts_schema(data.root)

    # If it's a date key itself (rare here, mostly keys)
    if isinstance(data, date):
        return data.isoformat()

    # Base case: just a value (float, int, str)
    return data


router = APIRouter()


@router.get('/income/{symbol}')
async def income(symbol, db: Session = Depends(get_db)):
    facts = get_facts(db)

    schema = build_facts_schema(facts)

    deconstructed = deconstruct_facts_schema(schema)
    print(deconstructed)
    return JSONResponse(
        content=deconstructed,
        status_code=status.HTTP_200_OK,
        media_type='application/json'
    )