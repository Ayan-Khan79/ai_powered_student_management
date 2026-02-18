import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def sample_student():
    return {
        "name": "Ayan Khan",
        "age": 21,
        "course": "Computer Science",
        "email": "ayan@example.com"
    }
    
import pytest

@pytest.fixture
def sample_professor():
    return {
        "pid": 101,
        "name": "Dr. John Smith",
        "experience": 12,
        "subject": "Computer Networks",
        "email": "john.smith@example.com"
    }
