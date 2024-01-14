from select import select

from config import settings
from sqlalchemy import Column, String, Integer, Sequence, insert
from modeles.good import Base, Classes, User
from sqlalchemy import create_engine, text


ur_s = settings.POSTGRES_DATABASE_URLS
#ur_a = settings.POSTGRES_DATABASE_URLA
#ur_p = 'postgresql://postgres:1234@localhost:5432/'
print(ur_s)

engine_s = create_engine(ur_s, echo=True)


def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)



def f():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from users;'))
        print(f"answer = {answer.all()}")

def f_bilder():
    with engine_s.connect() as conn:
        query_class_ids = select(Classes.id, Classes.class_name)
        class_ids = conn.execute(query_class_ids).fetchall()

        query = insert(User).values([
            {"name": "Roman Denisov", "hashed_password": "r2re2", "class_id": class_ids[0][0]},
            {"name": "Ivan Ivanov", "hashed_password": "tt432", "class_id": class_ids[1][0]}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(User)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")


def populate_classes_table():
    with engine_s.connect() as conn:
        query = insert(Classes).values([
            {"class_name": "1215i"},
            {"class_name": "1205u"}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(Classes)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")