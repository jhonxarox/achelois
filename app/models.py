from sqlalchemy import Column, Integer
from .database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
