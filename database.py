from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "mysql+mysqlconnector://root:123456789Helmi%40@localhost:3306/ENISo"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
