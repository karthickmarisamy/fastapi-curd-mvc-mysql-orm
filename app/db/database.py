from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

DATABASE_URL = "mysql+pymysql://root@localhost:3306/student"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base_model = declarative_base()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()