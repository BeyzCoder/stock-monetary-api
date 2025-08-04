from sqlalchemy.orm import Session
from app.api.v1.models.model_company import CompanyFact, CompanyTicker

def get_facts(symbol: str, state_type: str, db: Session):
    company_facts = db.query(CompanyFact).join(CompanyTicker).filter(
        CompanyTicker.ticker_symbol == symbol,
        CompanyFact.statement_type == state_type
    ).all()
    return company_facts