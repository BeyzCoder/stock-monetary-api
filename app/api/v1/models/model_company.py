from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.api.v1.db.database import Base

class CompanyTicker(Base):
    __tablename__ = 'company_tickers'

    id = Column(Integer, primary_key=True)
    sector = Column(String(250))
    industry = Column(String(250))
    ticker_symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String(250))
    currency = Column(String(10))

    facts = relationship("CompanyFact", back_populates="company", cascade="all, delete")


class CompanyFact(Base):
    __tablename__ = 'company_facts'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company_tickers.id', ondelete='CASCADE'))
    date = Column(Date, nullable=False)
    value = Column(Numeric)
    statement_type = Column(String(32))  # e.g., 'income'
    key_factor = Column(String(64))      # e.g., 'TotalRevenue', 'CostOfRevenue'
    form_type = Column(String(32))       # e.g., '10-K'

    company = relationship("CompanyTicker", back_populates="facts")
