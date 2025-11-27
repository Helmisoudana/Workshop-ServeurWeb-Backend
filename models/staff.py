from sqlmodel import SQLModel, Field

class Staff(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    fullname: str
    role: str     # ex: admin, direction, secrétariat
