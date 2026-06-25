import allure
import pytest

from helpers import generate_courier_data, register_courier, login_courier, delete_courier


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться - возвращается 200 и id")
    def test_login_courier_success_returns_200_and_id(self, courier):
        data, courier_id = courier
        response = login_courier(data["login"], data["password"])

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] is not None

    @allure.title("Авторизация без логина - возвращается 400")
    def test_login_courier_without_login_returns_400(self):
        response = login_courier("", "somepassword")

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Авторизация без пароля - возвращается 400")
    def test_login_courier_without_password_returns_400(self):
        response = login_courier("somelogin", "")

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Авторизация с неверным логином - возвращается 404")
    def test_login_courier_wrong_login_returns_404(self, courier):
        data, courier_id = courier
        response = login_courier("wronglogin_xyz", data["password"])

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Авторизация с неверным паролем - возвращается 404")
    def test_login_courier_wrong_password_returns_404(self, courier):
        data, courier_id = courier
        response = login_courier(data["login"], "wrongpassword_xyz")

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Авторизация несуществующего курьера - возвращается 404")
    def test_login_nonexistent_courier_returns_404(self):
        data = generate_courier_data()
        response = login_courier(data["login"], data["password"])

        assert response.status_code == 404
        assert "message" in response.json()
