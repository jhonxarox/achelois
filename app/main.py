from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine
from .database import engine, Base
from app.routers import feedback

app = FastAPI()

# Function to create the database tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Lifespan context manager for startup and shutdown events
@app.on_event("startup")
async def startup_event():
    await create_tables()

app.include_router(feedback.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Feedback API"}
