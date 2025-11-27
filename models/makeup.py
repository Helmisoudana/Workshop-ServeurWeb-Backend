from sqlmodel import SQLModel, Field

class MakeUpSession(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    session_id: int = Field(foreign_key="session.id")
    new_date: str
    reason: str | None = None
