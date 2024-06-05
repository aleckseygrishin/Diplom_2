import pytest
from burger_api import BurgerApi
from data import Data
from helper import Helper


class TestUserLogin:
    def test_user_login_status_code_success_email_and_name_correspond(self, create_and_delete_user,
                                                                      user_data_registration):
        login_user_data = Helper.modify_user_json(user_data_registration, Data.FIELD_USER[1])
        response = BurgerApi.login_user(login_user_data)
        assert (response.status_code == 200
                and response.json()["success"] is True
                and response.json()["user"]["email"] == login_user_data["email"]
                and response.json()["user"]["name"] == user_data_registration["name"]
                )

    @pytest.mark.parametrize('setting_param', Data.SETTING_EMAIL_OR_PASSWORD)
    def test_user_login_incorrect_data_success_is_false_message_error(self, create_and_delete_user,
                                                                      user_data_registration, setting_param):
        login_user_data = Helper.edit_user_data_login_incorrect(user_data_registration, setting_param, Data.FIELD_USER[1])
        response = BurgerApi.login_user(login_user_data)
        assert (response.status_code == 401 and response.json()["success"] is False
                and response.json()["message"] == "email or password are incorrect")
