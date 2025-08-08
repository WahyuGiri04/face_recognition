from sqlalchemy import Column, Integer, Boolean, DateTime, func
from core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, default=None)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    updated_by = Column(Integer, default=None)
    is_active  = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)