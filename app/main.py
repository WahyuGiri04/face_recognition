import uvicorn
from fastapi import FastAPI
from app.core.database import Base, engine
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.routers.employee_router import router as employee_router

# Create tables
Base.metadata.create_all(bind=engine)

# ---------- FASTAPI SETUP ----------
app = FastAPI(title=settings.APP_NAME, version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(employee_router)

@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running", "status": "OK"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)