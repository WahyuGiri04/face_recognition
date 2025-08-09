import uvicorn
from fastapi import FastAPI
from app.core.database import Base, engine
from app.core.config import settings

# Import models to ensure they are registered
from app.models.employee import Employee
from app.models.face import Face

# Import routers
from app.routers.employee_router import router as employee_router
from app.routers.face_router import router as face_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.include_router(employee_router)
app.include_router(face_router)

@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running", "status": "OK"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)