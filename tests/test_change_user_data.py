import allure
import pytest
from burger_api import BurgerApi
from data import Data
from helper import Helper


class TestUserLogin:
    @allure.title('Тест изменение данных пользователя с авторизацией')
    @allure.description('Изменение данных пользователя с авторизацией. '
                        'Ожидаем: статус код 200 и ответ об успешном измененнии данных')
    @pytest.mark.parametrize('name_field', Data.FIELD_USER[:2])
    def test_change_user_data_with_authorization(self, create_and_delete_user,
                                                 user_data_registration, name_field):
        access_token = Helper.get_access_token(create_and_delete_user)
        body_changed = Helper.edit_user_data_login_incorrect(user_data_registration, name_field, Data.FIELD_USER[2])
        response = BurgerApi.change_user(body_changed, access_token)
        assert (response.status_code == 200 and response.json()["success"] is True
                and response.json()["user"][name_field] == body_changed[name_field])

    @allure.title('Тест изменение данных пользователя без авторизацией')
    @allure.description('Изменение данных пользователя без авторизацией. '
                        'Ожидаем: статус код 401 и ответ об ошибке')
    @pytest.mark.parametrize('name_field', Data.FIELD_USER[:2])
    def test_change_user_data_without_authorization(self, user_data_registration, name_field):
        body_changed = Helper.edit_user_data_login_incorrect(user_data_registration, name_field, Data.FIELD_USER[2])
        response = BurgerApi.change_user(body_changed)
        assert (response.status_code == 401 and response.json()["success"] is False
                and response.json()["message"] == Data.CHECK_ERR_YOU_SHOULD_BE_AUTH)
