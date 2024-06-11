import allure
from faker import Faker


class Helper:
    @staticmethod
    @allure.step('Создаем данные для регистрации пользователя')
    def random_user():
        faker = Faker()
        return {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }

    @staticmethod
    @allure.step('Вызываем метод удаления передаваемого поля из JSON')
    def modify_user_json(body, field_del):
        body_copy = body.copy()
        del body_copy[field_del]
        return body_copy

    @staticmethod
    @allure.step('Вызываем метод изменение данных пользователя')
    def edit_user_data_login_incorrect(body, field_change, field_del):
        data_incorrect = Helper.modify_user_json(body, field_del)
        symbol = '!'
        data_incorrect[field_change] = data_incorrect[field_change] + symbol

        return data_incorrect

    @staticmethod
    @allure.step('Вызываем метод получения accessToken из запроса')
    def get_access_token(response):
        access_token = response.json()["accessToken"]
        return access_token

    @staticmethod
    @allure.step('Вызываем метод формирования данных для заказа')
    def get_ingredients_list(response):
        list_of_return = []
        for i in range(2):
            list_of_return.append(response.json()["data"][i]["_id"])
        return {"ingredients": list_of_return}
