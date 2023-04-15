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
    domain_url = "https://mobimg.b-cdn.net/"
    full_url = f"{domain_url}v3/fetch/71/71ab2b99214efab5efe341d0a844a47c.jpeg"
    response = client.post("/predict/",
                           json={"url": full_url})
    assert response.status_code == 200
    assert response.json() == "Siamese cat, Siamese"
