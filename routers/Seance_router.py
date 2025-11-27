from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models.Seance import Seance as SeanceModel

router = APIRouter(prefix="/seance", tags=["Sessions"])

@router.post("/")
def create_session(session_obj: SeanceModel, session: Session = Depends(get_session)):
    session.add(session_obj)
    session.commit()
    session.refresh(session_obj)
    return session_obj

@router.get("/")
def get_sessions(session: Session = Depends(get_session)):
    return session.exec(select(SeanceModel)).all()

@router.get("/{session_id}")
def get_session(session_id: int, session: Session = Depends(get_session)):
    return session.get(SeanceModel, session_id)

@router.put("/{session_id}")
def update_session(session_id: int, data: SeanceModel, session: Session = Depends(get_session)):
    session_obj = session.get(SeanceModel, session_id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(session_obj, key, value)
    session.add(session_obj)
    session.commit()
    session.refresh(session_obj)
    return session_obj

@router.delete("/{session_id}")
def delete_session(session_id: int, session: Session = Depends(get_session)):
    session_obj = session.get(SeanceModel, session_id)
    session.delete(session_obj)
    session.commit()
    return {"message": "Session deleted"}
