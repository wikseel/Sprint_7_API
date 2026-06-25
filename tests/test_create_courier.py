import allure
import pytest

from helpers import generate_courier_data, register_courier, login_courier, delete_courier
from urls import COURIER_URL


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать - возвращается 201 и ok:true")
    def test_create_courier_success_returns_201_and_ok_true(self):
        data = generate_courier_data()
        response = register_courier(data)

        # Удаляем после теста
        login_response = login_courier(data["login"], data["password"])
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров - возвращается 409")
    def test_create_duplicate_courier_returns_409(self):
        data = generate_courier_data()
        register_courier(data)
        response = register_courier(data)

        # Удаляем после теста
        login_response = login_courier(data["login"], data["password"])
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)

        assert response.status_code == 409

    @allure.title("Нельзя создать курьера с уже существующим логином - возвращается ошибка")
    def test_create_courier_with_existing_login_returns_error(self):
        data = generate_courier_data()
        register_courier(data)

        data2 = generate_courier_data()
        data2["login"] = data["login"]
        response = register_courier(data2)

        # Удаляем после теста
        login_response = login_courier(data["login"], data["password"])
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)

        assert response.status_code == 409
        assert "message" in response.json()

    @allure.title("Нельзя создать курьера без логина - возвращается 400")
    def test_create_courier_without_login_returns_400(self):
        data = generate_courier_data()
        del data["login"]
        response = register_courier(data)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Нельзя создать курьера без пароля - возвращается 400")
    def test_create_courier_without_password_returns_400(self):
        data = generate_courier_data()
        del data["password"]
        response = register_courier(data)

        assert response.status_code == 400
        assert "message" in response.json()
