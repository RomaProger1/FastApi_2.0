from config import setttings
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy import create_engine, text
from modeles.good import Base

from sqlalchemy import create_engine, text


#setttings.DATABASE_URL = 'sqlite:///./test02.db'
#engine = create_engine(setttings.POSTGRES_DATABASE_URL)

#ur_p = "postgresql+://postgres:900@localhost:5432/dbtest04"

ur_p = setttings.POSTGRES_DATABASE_URLS
ur_p = setttings.POSTGRES_DATABASE_URLA

print(ur_p)

engine = create_engine(ur_p, echo=True)

with engine.begin() as conn:
    answer = conn.execute(text("select version()"))
    print(f"answer = {answer.all ()}")