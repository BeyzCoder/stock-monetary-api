from sqlalchemy.orm import Session
from app.api.v1.models.model_statements import CompanyFact, CompanyTicker

def get_facts(db: Session):
    company_facts = db.query(CompanyFact).join(CompanyTicker).filter(
        CompanyTicker.ticker_symbol == "AAPL"
    ).all()
    return company_facts