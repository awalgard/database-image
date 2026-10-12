from main import user


def check_kvartira_user(user_: str) -> int:
    if user_ == "Nikita":
        return print("Квартира номер 1")
    else:
        return print("Пользователь не найден")