from config import settings
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy import create_engine, text
from modeles.good import Base

from sqlalchemy import create_engine, text


#setttings.DATABASE_URL = 'sqlite:///./test02.db'
#engine = create_engine(setttings.POSTGRES_DATABASE_URL)

#ur_p = "postgresql+://postgres:900@localhost:5432/dbtest04"

ur_s = settings.POSTGRES_DATABASE_URLS
ur_a = settings.POSTGRES_DATABASE_URLA

print(ur_s)

engine = create_engine(ur_s, echo=True)

def create_tables(engine_s=None):
    Base.metadata.create_all(bind=engine_s)

def f(engine_s=None):
    with engine_s.connect() as conn:
        answer = conn.execute(text("select version()"))
        print(f"answer = {answer.all()}")