import allure

from helper import Helper
from burger_api import BurgerApi


class TestGetOrder:
    @allure.title('Тест получение заказа пользователя')
    @allure.description('Ожидаем: статус код 200, ответ об успешном создании заказа и количество заказов больше 0')
    def test_get_order_user_authorization_success_is_true(self, create_and_delete_user, create_order_with_auth):
        token = Helper.get_access_token(create_and_delete_user)
        response = BurgerApi.get_order_user(token)
        assert response.status_code == 200 and response.json()["success"] is True and len(response.json()["orders"]) > 0

    @allure.title('Тест получение заказа пользователя без авторизации')
    @allure.description('Ожидаем: статус код 401, success = False и сообщение об ошибке')
    def test_get_order_user_without_auth_message_error(self, create_and_delete_user, create_order_with_auth):
        response = BurgerApi.get_order_user()
        assert (response.status_code == 401 and response.json()["success"] is False
                and response.json()["message"] == "You should be authorised")
