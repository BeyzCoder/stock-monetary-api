from pydantic import RootModel
from typing import Dict
from datetime import date

class KeyFactorData(RootModel):
    # Mapping: date → value
    root: Dict[date, float]

class StatementTypeSchema(RootModel):
    # Mapping: key_factor → { date: value }
    root: Dict[str, KeyFactorData]

class CompanyFactsSchema(RootModel):
    # Mapping: statement_type → { key_factor: { date: value } }
    root: Dict[str, StatementTypeSchema]
