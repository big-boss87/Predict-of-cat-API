from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

response_root = client.get("/")
response_demo = client.get("/demo/")


url = ("https://mobimg.b-cdn.net/"
       + "v3/fetch/71/"
       + "71ab2b99214efab5efe341d0a844a47c.jpeg")
response_predict = client.post("/predict/", json={"url": url})


first_image = ("https://t3.gstatic.com"
               + "/licensed-image?q=tbn:"
               + "ANd9GcRoT6NNDUONDQmlthWrqIi_"
               + "frTjsjQT4UZtsJsuxqxLiaFGNl5s3_"
               + "pBIVxS6-VsFUP_")
second_image = ("https://cdnn21.img.ria.ru/"
                + "images/144814/13/1448141397_"
                + "0:219:4256:2613_600x0_80_0_0_"
                + "daca8ef930216c2914360b4561ec4c30.jpg")
response_predict_list = client.post("/predict-list/",
                                    json={"urls": [
                                         first_image, second_image]})


# Тест кейсы корневого пути
def test_read_main_root_code():
    assert response_root.status_code == 200


def test_read_main_root_not_empty():
    assert len(response_root.json()['message']) != 0


def test_read_main_root_original_len():
    assert len(response_root.json()['message']) == 34


def test_read_main_root_text_value():
    assert response_root.json()[
                        'message'] == "This is neural network's main page"


# Тест-кейсы по демо предсказанию
def test_read_main_demo_code():
    assert response_demo.status_code == 200


def test_read_main_demo_not_empty():
    assert len(response_demo.json()) != 0


def test_read_main_demo_original_len():
    assert len(response_demo.json()) == 12


def test_read_main_demo_text_value():
    assert response_demo.json() == 'Egyptian cat'


# Тест-кейсы по предсказанию одного изображения
def test_read_main_predict_code():
    assert response_predict.status_code == 200


def test_read_main_predict_not_empty():
    assert len(response_predict.json()) != 0


def test_read_main_predict_original_len():
    assert len(response_predict.json()) == 20


def test_read_main_predict_text_value():
    assert response_predict.json() == "Siamese cat, Siamese"


# Тест-кейсы по предсказаниям списка изображений
def test_read_main_predict_list_code():
    assert response_predict_list.status_code == 200


def test_read_main_predict_list_not_empty():
    assert len(response_predict_list.json()) != 0


def test_read_main_predict_list_original_len():
    assert len(response_predict_list.json()) == 2


def test_read_main_predict_list_text_value():
    assert response_predict_list.json() == [
        'tabby, tabby cat', 'Egyptian cat'
    ]
