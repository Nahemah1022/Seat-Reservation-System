from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI:str = 'mysql+pymysql://root:ZFhLrUg1QV9FzUy4x8RT@db/master'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
meta = MetaData()

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

def getDBSession():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
