from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declaractive_base
from app.api.v1.config import DB_CONFIG

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(*DB_CONFIG))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declaractive_base()