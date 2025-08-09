import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.database import Base, engine
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.routers.employee_router import router as employee_router
from app.routers.face_recognition import router as face_recognition_router
from app.schemas.base_response import BaseResponse
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

# Global exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    response = BaseResponse.bad_request("Invalid request data")
    return JSONResponse(
        status_code=400,
        content=response.dict()
    )

# Global exception handler for general exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    response = BaseResponse.error("Internal server error")
    return JSONResponse(
        status_code=500,
        content=response.dict()
    )

app.include_router(employee_router)
app.include_router(face_recognition_router)

@app.get("/", response_model=BaseResponse[dict])
def root():
    return BaseResponse.success(
        data={"app_name": settings.APP_NAME, "version": "1.0.0"},
        message="API is running successfully"
    )

@app.get("/health", response_model=BaseResponse[dict])
def health_check():
    return BaseResponse.success(
        data={"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"},
        message="Health check passed"
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)