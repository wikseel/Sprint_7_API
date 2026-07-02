import allure

import requests

from urls import ORDERS_URL


@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов - возвращается 200 и список заказов")
    def test_get_orders_returns_200_and_orders_list(self):
        response = requests.get(ORDERS_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
