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
sqlalchemy.url = postgresql+asyncpg://username:password@localhost/databasename
```

3. Create and apply migrations:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Running the Application
```bash
uvicorn app.main:app --reload
```

### How to hit the API
To hit the API on the backend directly, you can use tools like curl, Postman, or Python scripts. Here are examples of how you can do this using each method:

#### Using curl
You can use curl to send a POST request to the backend API. Open your terminal and run:

```bash
curl -X POST "http://127.0.0.1:8000/feedback/" -H "Content-Type: application/json" -d '{"rating": 5}'
```

#### Using Postman
1. Open Postman and create a new POST request.
2. Enter the URL: `http://127.0.0.1:8000/feedback/`
3. Set the Headers:
```json
Key: Content-Type
Value: application/json
```
4. Set the Body to raw JSON and enter the following payload:
```json
{
  "rating": 5
}
```
5. Send the Request and check the response.

#### Using Python Script
You can also use a Python script with the requests library to send a POST request to the API:

```python
import requests

url = "http://127.0.0.1:8000/feedback/"
payload = {
    "rating": 5
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())
```
Instructions for Python Script:
- Install the requests library if you don't have it installed:
```bash
pip install requests
```
- Run the script:
``` bash
python script_name.py
```

If you find Cors on file `app/main.py` :
```python
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:5173"],  # Update this with your frontend URL and backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

