from sqlalchemy import Column, Integer, String
from database import Base

class StudyPlan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    subjects = Column(String)
    hours = Column(Integer)
    plan = Column(String)