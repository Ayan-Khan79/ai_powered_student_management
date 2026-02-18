import pytest


# Home Route Test
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to student management Api"
    }


# Student Tests

#Creat student
def test_create_student(client, sample_student):
    response = client.post("/students", json=sample_student)

    assert response.status_code == 200
    assert response.json()["name"] == sample_student["name"]
    assert response.json()["age"] == sample_student["age"]
    assert response.json()["email"] == sample_student["email"]



#Get all Students
def test_get_students(client):
    
    response = client.get("/students")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >=1


def test_get_student_by_id(client,sample_student):
    response = client.get("/students/0")
    assert response.status_code == 200
    assert response.json()["name"] == sample_student["name"]


def test_update_student(client):
    response = client.put("/students/0", json={
        "name": "Updated Ayan",
        "age": 22,
        "course": "AI"
    })

    assert response.status_code == 200
    assert response.json()["message"] == "Student updated successfully"


def test_delete_student(client):
    response = client.delete("/students/0")
    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"


def test_student_not_found(client):
    response = client.get("/students/100")
    assert response.status_code == 404


# --------------------------
# Professor Tests
# --------------------------

def test_create_professor(client, sample_professor):
    response = client.post("/professor", json=sample_professor)

    assert response.status_code == 200
    assert response.json()["name"] == sample_professor["name"]
    assert response.json()["pid"] == sample_professor["pid"]



def test_get_professors(client):
    response = client.get("/professors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# --------------------------
# Search Test
# --------------------------

def test_search_student(client):
    # First create student
    client.post("/students", json={
        "name": "Rahul",
        "age": 20,
        "course": "Math"
    })

    response = client.get("/search?name=Rahul")
    assert response.status_code == 200
    assert response.json()["count"] >= 1


# --------------------------
# NLP Test
# --------------------------

def test_analyze_feedback(client):
    response = client.post("/analyze-feedback", json={
        "text": "This API is amazing"
    })

    assert response.status_code == 200
    assert "Result" in response.json()
