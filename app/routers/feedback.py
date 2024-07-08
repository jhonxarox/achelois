from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/feedback",
    tags=["feedback"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Feedback)
async def create_feedback(feedback: schemas.FeedbackCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_feedback(db=db, feedback=feedback)
