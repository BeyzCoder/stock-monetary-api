from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.api.v1.config import DB_CONFIG

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(*DB_CONFIG))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()  # ← Creates a session
    try:
        yield db          # ← Passed into route via Depends
    finally:
        db.close()