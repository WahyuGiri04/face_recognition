from models.base import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Employee(BaseModel):
    __tablename__ = 'employee'

    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    face = relationship('Face', back_populates='employee')