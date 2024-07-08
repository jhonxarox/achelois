from pydantic import BaseModel

class FeedbackBase(BaseModel):
    rating: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
