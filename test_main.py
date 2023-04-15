from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_main_demo():
    response = client.get("/demo/")
    assert response.status_code == 200
    assert response.json() == 'Egyptian cat'

def test_read_main_predict():
    response = client.post("/predict/",
                           json={"url":
                            "https://mobimg.b-cdn.net/v3/fetch/71/71ab2b99214efab5efe341d0a844a47c.jpeg"})
    assert response.status_code == 200
    assert response.json() == "Siamese cat, Siamese"