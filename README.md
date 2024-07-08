# Feedback Form API (Achelois)

## Development Setup

### Clone the Repository
   ```bash
   git clone <repository-url> #can use ssh or https
   cd achelois
   ```

### Python Environment
1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### PostgreSQL Database
1. Install PostgreSQL:

```bash
brew install postgresql
```

2. Start PostgreSQL service:

```bash
brew services start postgresql
```

3. Create a database:

```sql
CREATE DATABASE mydatabase;
```

### Environment Variables
1. Create a .env file:

```bash
touch .env
```

2. Add the following environment variables to the .env file:

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost/databasename
DATABASE_URL_SYNC=postgresql://username:password@localhost/databasename
```

### Alembic Migrations
1. Initialize Alembic:

```bash
alembic init alembic
```

2. Configure Alembic on `alembic.ini`: 

```ini
sqlalchemy.url = postgresql+asyncpg://jhonarox:test123@localhost/ttdatabase
```

3. Create and apply migrations:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Running the Application
```bash
uvicorn app.main:app --reload
```

### Running Tests
1. Install testing libraries:

```bash
pip install pytest pytest-asyncio httpx
```
2. Run tests:

```bash
pytest
```

## Project Structure
```bash
feedback_form/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       └── feedback.py
├── tests/
│   └── test_feedback.py
├── .env
├── requirements.txt
└── README.md
```
## API Documentation
List of API endpoints and their usage can be accessed via Swagger UI at http://127.0.0.1:8000/docs.

## License
Project license information.