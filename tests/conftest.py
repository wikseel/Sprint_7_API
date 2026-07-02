import pytest

from helpers import generate_courier_data, register_courier, login_courier, delete_courier


@pytest.fixture
def registered_courier_data():
    data = generate_courier_data()
    response = register_courier(data)

    login_response = login_courier(data["login"], data["password"])
    courier_id = login_response.json().get("id")

    yield data, response, courier_id

    if courier_id:
        delete_courier(courier_id)
