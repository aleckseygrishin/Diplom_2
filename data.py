from helper import Helper


class Data:
    USER_REGISTRATION_EMPTY_FIELD = [
        {
            "email": "",
            "password": "123456789",
            "name": "Alexey"
        },
        {
            "email": "alexeyy.grishin@ya.ru",
            "password": "",
            "name": "Alexey"
        },
        {
            "email": "alexeyy.grishin@ya.ru",
            "password": "123456789",
            "name": ""
        }
    ]

    SETTING_EMAIL_OR_PASSWORD = [
        'email',
        'password'
    ]

    FIELD_USER = [
        'email',
        'name',
        'password'
    ]

    INCORRECT_INGREDIENT = {
        "ingredients": [""]
    }
