from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'API', 'RiddlesApi')))

from crudRiddles import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Api direcionado para manipulação de enigmas."}


def test_create_riddle():
    response = client.post("/riddles/set", json={"id": 1, "description": "example", "question": "example question", "response": "example response"})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == True


def test_read_riddle():
    client.post("/riddles/set", json={"id": 1, "description": "example", "question": "example question", "response": "example response"})
    response = client.get("/riddles/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == False


def test_read_riddles():
    response = client.get("/riddles")
    assert response.status_code == 200


def test_update_riddle():
    response = client.put("/riddles/alter/1", json={"id": 1, "description": "example 2", "question": "example question 2", "response": "example response 2"})
    assert response.status_code == 200
