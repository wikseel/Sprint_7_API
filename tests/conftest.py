import pytest

from helpers import generate_courier_data, register_courier, login_courier, delete_courier


@pytest.fixture
def courier():
    # Создаёт курьера перед тестом и удаляет после
    data = generate_courier_data()
    register_courier(data)

    response = login_courier(data["login"], data["password"])
    courier_id = response.json().get("id")

    yield data, courier_id

    if courier_id:
        delete_courier(courier_id)
