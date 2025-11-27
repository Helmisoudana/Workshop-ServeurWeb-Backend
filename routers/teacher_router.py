from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models.teacher import Teacher

router = APIRouter(prefix="/teachers", tags=["Teachers"])

@router.post("/")
def create_teacher(teacher: Teacher, session: Session = Depends(get_session)):
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    return teacher

@router.get("/")
def get_teachers(session: Session = Depends(get_session)):
    return session.exec(select(Teacher)).all()

@router.get("/{teacher_id}")
def get_teacher(teacher_id: int, session: Session = Depends(get_session)):
    return session.get(Teacher, teacher_id)

@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, data: Teacher, session: Session = Depends(get_session)):
    teacher = session.get(Teacher, teacher_id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(teacher, key, value)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    return teacher

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, session: Session = Depends(get_session)):
    teacher = session.get(Teacher, teacher_id)
    session.delete(teacher)
    session.commit()
    return {"message": "Teacher deleted"}
