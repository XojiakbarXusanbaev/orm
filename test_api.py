from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
