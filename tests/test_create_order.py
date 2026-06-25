import allure
import pytest

import requests

from urls import ORDERS_URL


ORDER_BASE = {
    "firstName": "Тест",
    "lastName": "Тестов",
    "address": "ул. Тверская, 1",
    "metroStation": 4,
    "phone": "+79991234567",
    "rentTime": 3,
    "deliveryDate": "2024-12-01",
    "comment": "Тестовый заказ",
}


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [],
    ], ids=["black", "grey", "both_colors", "no_color"])
    def test_create_order_with_color_returns_201_and_track(self, color):
        payload = {**ORDER_BASE, "color": color}
        response = requests.post(ORDERS_URL, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
