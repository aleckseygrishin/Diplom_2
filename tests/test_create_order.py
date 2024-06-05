import pytest
from data import Data
from burger_api import BurgerApi


class TestCreateOrder:
    def test_create_order_without_auth_hash_ingredients_is_not_empty(self, create_order):
        assert create_order.status_code == 200 and create_order.json()["success"] is True

    def test_create_order_without_auth_hash_ingredients_is_empty(self):
        response = BurgerApi.create_order()
        assert (response.status_code == 400 and response.json()["success"] is False
                and response.json()["message"] == "Ingredient ids must be provided")

    def test_create_order_without_auth_hash_ingredients_incorrect(self):
        response = BurgerApi.create_order(Data.INCORRECT_INGREDIENT)
        assert (response.status_code == 500)

    def test_create_order_with_auth(self, create_order_with_auth, user_data_registration):
        assert (create_order_with_auth.status_code == 200 and create_order_with_auth.json()["success"] is True
                and create_order_with_auth.json()["order"]["owner"]["email"] == user_data_registration["email"])
