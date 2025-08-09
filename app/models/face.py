from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Face(Base):
    __tablename__ = "face"
    __table_args__ = {"schema": "user_management"}

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    employee_id = Column(Integer, ForeignKey("user_management.employee.id", ondelete="CASCADE"), nullable=False)
    image_base64 = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    created_by = Column(Integer)
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
