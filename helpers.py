import random
import string

import requests

from urls import COURIER_URL, COURIER_LOGIN_URL


def generate_random_string(length=10):
    # Генерирует случайную строку из букв нижнего регистра
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_data():
    # Генерирует данные нового курьера
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


def register_courier(data):
    # Регистрирует курьера и возвращает ответ
    return requests.post(COURIER_URL, json=data)


def login_courier(login, password):
    # Авторизует курьера и возвращает ответ
    return requests.post(COURIER_LOGIN_URL, json={"login": login, "password": password})


def delete_courier(courier_id):
    # Удаляет курьера по id
    requests.delete(f"{COURIER_URL}/{courier_id}")
