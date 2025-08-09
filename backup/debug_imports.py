#!/usr/bin/env python3

# Debug script to test imports
try:
    print("Testing imports...")
    
    print("1. Testing schemas...")
    from app.schemas.face import FaceCreate, FaceUpdate, FaceResponse
    from app.schemas.face_recognition import VerifyRequest, VerifyResponse
    print("   ✓ Schemas imported successfully")
    
    print("2. Testing models...")
    from app.models.employee import Employee
    print("   ✓ Models imported successfully")
    
    print("3. Testing repositories...")
    from app.repositories.employee_repository import create, get_all, get_by_id, update, delete
    from app.repositories.face_repository import create as face_create, get_all as face_get_all
    print("   ✓ Repositories imported successfully")
    
    print("4. Testing services...")
    from app.services.employee_service import create_employee, get_all_employees
    from app.services.face_service import create_face, get_all_faces
    print("   ✓ Services imported successfully")
    
    print("5. Testing routers...")
    from app.routers.employee_router import router as employee_router
    print("   ✓ Routers imported successfully")
    
    print("6. Testing core...")
    from app.core.config import settings
    from app.core.database import get_db
    print("   ✓ Core imported successfully")
    
    print("\n✅ All imports successful!")
    print("You can now run: python run.py")
    
except Exception as e:
    print(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()