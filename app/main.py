from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import employee, face
from app.routers import employee_router, face_router
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(employee_router.router)
app.include_router(face_router.router)

@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}
