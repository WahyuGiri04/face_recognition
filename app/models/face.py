from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Face(BaseModel):
    __tablename__ = 'face'

    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    image_base64 = Column(Text, nullable=False)
    employee = relationship('Employee', back_populates='face')