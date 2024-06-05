import requests
from urls import Urls


class BurgerApi:
    @staticmethod
    def create_user(body):
        response = requests.post(Urls.USER_REGISTRATION_URL, json=body)
        return response

    @staticmethod
    def delete_user(token):
        response = requests.delete(Urls.DELETE_OR_PATCH_USER_URL, headers={'Authorization': token})
        return response

    @staticmethod
    def login_user(body):
        response = requests.post(Urls.USER_LOGIN_URL, json=body)
        return response

    @staticmethod
    def change_user(body, token=None):
        if token is None:
            response = requests.patch(Urls.DELETE_OR_PATCH_USER_URL, json=body)
        else:
            response = requests.patch(Urls.DELETE_OR_PATCH_USER_URL, json=body, headers={'Authorization': token})
        return response

    @staticmethod
    def get_ingredients():
        response = requests.get(Urls.GET_INGREDIENTS_URL)
        return response

    @staticmethod
    def create_order(body=None, token=None):
        if body is None:
            response = requests.post(Urls.CREATE_ORDER_URL)
        else:
            if token is not None:
                response = requests.post(Urls.CREATE_ORDER_URL, json=body, headers={"Authorization": token})
            else:
                response = requests.post(Urls.CREATE_ORDER_URL, json=body)
        return response
