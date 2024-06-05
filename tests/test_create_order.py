import allure

from data import Data
from burger_api import BurgerApi


class TestCreateOrder:
    @allure.title('Тест создание заказа без авторизации')
    @allure.description('Ожидаем: статус код 200 и ответ об успешном создании заказа')
    def test_create_order_without_auth_hash_ingredients_is_not_empty(self, create_order):
        assert create_order.status_code == 200 and create_order.json()["success"] is True

    @allure.title('Тест создание заказа без авторизации, без передачи ингредиентов в теле запроса')
    @allure.description('Ожидаем: статус код 400 и сообщение об ошибке в ответе')
    def test_create_order_without_auth_hash_ingredients_is_empty(self):
        response = BurgerApi.create_order()
        assert (response.status_code == 400 and response.json()["success"] is False
                and response.json()["message"] == "Ingredient ids must be provided")

    @allure.title('Тест создание заказа без авторизации, hash ингредиента - некорректный')
    @allure.description('Ожидаем: статус код 500')
    def test_create_order_without_auth_hash_ingredients_incorrect(self):
        response = BurgerApi.create_order(Data.INCORRECT_INGREDIENT)
        assert (response.status_code == 500)

    @allure.title('Тест создание заказа с авторизацией')
    @allure.description('Ожидаем: статус код 200 и ответ об успешном создании заказа, '
                        'и поле email ответа совпадает с email пользователя')
    def test_create_order_with_auth(self, create_order_with_auth, user_data_registration):
        assert (create_order_with_auth.status_code == 200 and create_order_with_auth.json()["success"] is True
                and create_order_with_auth.json()["order"]["owner"]["email"] == user_data_registration["email"])
