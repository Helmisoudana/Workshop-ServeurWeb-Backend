from fastapi import FastAPI
from database import create_db_and_tables
from routers.student_router import router as student_router
from routers.teacher_router import router as teacher_router
from routers.Seance_router import router as seance_router
from routers.staff_router import router as staff_router
from routers.makeup_routes import router as makeup_router
app = FastAPI(
    title="School Management API",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(seance_router)
app.include_router(staff_router)

app.include_router(makeup_router)
