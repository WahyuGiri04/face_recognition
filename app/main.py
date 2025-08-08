from fastapi import FastAPI
from core.database import engine
from models import base
from routers import employee_router

# Create tables
base.BaseModel.metadata.create_all(bind=engine)

app = FastAPI(title="Employee-Face API")
app.include_router(employee_router.router)