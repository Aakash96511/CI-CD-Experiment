
from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert b"My CI/CD Pipeline Project" in response.data


def test_health():
    tester = app.test_client()
    response = tester.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["message"] == "Application is healthy"
