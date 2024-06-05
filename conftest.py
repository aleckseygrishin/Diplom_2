import allure
import pytest

from burger_api import BurgerApi
from helper import Helper


@pytest.fixture(scope='function')
@allure.step('Вызываем фикстуру (создание и удаление по окончанию теста пользователя)')
def create_and_delete_user(user_data_registration):
    create = BurgerApi.create_user(user_data_registration)
    token = Helper.get_access_token(create)

    yield create

    BurgerApi.delete_user(token)


@pytest.fixture(scope='function')
@allure.step('Вызываем фикстуру (создание json для регистрации пользователя)')
def user_data_registration():
    return Helper.random_user()


# В документации отсутствует удаление заказа, поэтому return, без удаления
@pytest.fixture(scope='function')
@allure.step('Вызываем фикстуру (создание заказа, без авторизации)')
def create_order():
    get_ingredients_response = BurgerApi.get_ingredients()
    order_body = Helper.get_ingredients_list(get_ingredients_response)
    create_order = BurgerApi.create_order(order_body)

    return create_order


@pytest.fixture(scope='function')
@allure.step('Вызываем фикстуру (создание заказа, с авторизацией)')
def create_order_with_auth(create_and_delete_user):
    token = Helper.get_access_token(create_and_delete_user)
    get_ingredients = BurgerApi.get_ingredients()
    order = Helper.get_ingredients_list(get_ingredients)
    create = BurgerApi.create_order(order, token)

    return create
