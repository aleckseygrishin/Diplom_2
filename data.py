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

    CHECK_ERR_YOU_SHOULD_BE_AUTH = "You should be authorised"
    CHECK_ERR_INGREDIENTS_ID = "Ingredient ids must be provided"
    CHECK_ERR_EMAIL_INCORRECT = "email or password are incorrect"
    CHECK_ERR_USER_EXIST = "User already exists"
    CHECK_REQUIRED_FIELDS = "Email, password and name are required fields"
