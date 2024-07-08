import pytest
from httpx import AsyncClient
from app.main import app
from app.database import get_db, Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Use PostgreSQL for testing
DATABASE_URL = "postgresql+asyncpg://jhonarox:test123@localhost/testdb"
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Create the database schema
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Drop the database schema after tests
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_feedback(async_client):
    response = await async_client.post("/feedback/", json={"rating": 5})
    assert response.status_code == 200
    assert response.json()["rating"] == 5
