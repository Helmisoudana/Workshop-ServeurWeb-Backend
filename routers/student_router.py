from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models.student import Student

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def create_student(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@router.get("/")
def get_students(session: Session = Depends(get_session)):
    return session.exec(select(Student)).all()

@router.get("/{student_id}")
def get_student(student_id: int, session: Session = Depends(get_session)):
    return session.get(Student, student_id)

@router.put("/{student_id}")
def update_student(student_id: int, data: Student, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(student, key, value)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@router.delete("/{student_id}")
def delete_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    session.delete(student)
    session.commit()
    return {"message": "Student deleted"}
