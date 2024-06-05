import pytest
from data import Data
from burger_api import BurgerApi


class TestUserRegistration:
    def test_user_registration_status_code_success(self, create_and_delete_user):
        assert create_and_delete_user.status_code == 200 and create_and_delete_user.json()["success"] is True

    def test_user_registration_user_exist_success_is_false(self, create_and_delete_user, user_data_registration):
        second_registration = BurgerApi.create_user(user_data_registration)
        assert (second_registration.status_code == 403
                and second_registration.json()["success"] is False
                and second_registration.json()["message"] == "User already exists")

    @pytest.mark.parametrize('body', [pytest.param(Data.USER_REGISTRATION_EMPTY_FIELD[0]),
                                      pytest.param(Data.USER_REGISTRATION_EMPTY_FIELD[1]),
                                      pytest.param(Data.USER_REGISTRATION_EMPTY_FIELD[2])])
    def test_user_registration_empty_field_success_is_false(self, body):
        create = BurgerApi.create_user(body)
        assert (create.status_code == 403
                and create.json()["success"] is False
                and create.json()["message"] == "Email, password and name are required fields")
