from sqlmodel import SQLModel, Field, Relationship

class Seance(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    subject: str
    room: str
    teacher_id: int = Field(foreign_key="teacher.id")
