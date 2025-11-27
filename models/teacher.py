from sqlmodel import SQLModel, Field

class Teacher(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    specialty: str
