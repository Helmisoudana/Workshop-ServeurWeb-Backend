from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models.staff import Staff

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.post("/")
def create_staff(staff: Staff, session: Session = Depends(get_session)):
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff

@router.get("/")
def get_staff(session: Session = Depends(get_session)):
    return session.exec(select(Staff)).all()

@router.get("/{staff_id}")
def get_single_staff(staff_id: int, session: Session = Depends(get_session)):
    return session.get(Staff, staff_id)

@router.put("/{staff_id}")
def update_staff(staff_id: int, data: Staff, session: Session = Depends(get_session)):
    staff = session.get(Staff, staff_id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(staff, key, value)
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff

@router.delete("/{staff_id}")
def delete_staff(staff_id: int, session: Session = Depends(get_session)):
    staff = session.get(Staff, staff_id)
    session.delete(staff)
    session.commit()
    return {"message": "Staff deleted"}
