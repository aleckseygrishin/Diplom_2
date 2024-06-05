import allure
import requests

from urls import Urls


class BurgerApi:
    @staticmethod
    @allure.step('Возвращаем ответ на запрос (регистрация пользователя)')
    def create_user(body):
        response = requests.post(Urls.USER_REGISTRATION_URL, json=body)
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (удаление пользователя)')
    def delete_user(token):
        response = requests.delete(Urls.DELETE_OR_PATCH_USER_URL, headers={'Authorization': token})
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (авторизация в системе)')
    def login_user(body):
        response = requests.post(Urls.USER_LOGIN_URL, json=body)
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (изменение данных пользователя)')
    def change_user(body, token=None):
        if token is None:
            response = requests.patch(Urls.DELETE_OR_PATCH_USER_URL, json=body)
        else:
            response = requests.patch(Urls.DELETE_OR_PATCH_USER_URL, json=body, headers={'Authorization': token})
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (список ингредиентов)')
    def get_ingredients():
        response = requests.get(Urls.GET_INGREDIENTS_URL)
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (создание заказа)')
    def create_order(body=None, token=None):
        if body is None:
            response = requests.post(Urls.CREATE_OR_GET_ORDER_URL)
        else:
            if token is not None:
                response = requests.post(Urls.CREATE_OR_GET_ORDER_URL, json=body, headers={"Authorization": token})
            else:
                response = requests.post(Urls.CREATE_OR_GET_ORDER_URL, json=body)
        return response

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (список заказов пользователя)')
    def get_order_user(token=None):
        if token is not None:
            response = requests.get(Urls.CREATE_OR_GET_ORDER_URL, headers={"Authorization": token})
        else:
            response = requests.get(Urls.CREATE_OR_GET_ORDER_URL)
        return response
