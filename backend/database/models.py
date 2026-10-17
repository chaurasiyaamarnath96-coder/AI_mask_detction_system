from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String,Float, DateTime, ForeignKey

class Base(DeclarativeBase):
    pass

class MuskDetection(Base):
    __tablename__ = "musk_detections"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    total_faces = Column(Integer, nullable=False)
    masked = Column(Integer, nullable=False)
    unmasked = Column(Integer, nullable=False)
    incorrectly_masked = Column(Integer, nullable=False)    
    compliance_percentage = Column(Float, nullable=False)