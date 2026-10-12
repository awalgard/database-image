user = "Nikita"


def user_check_name(user: str) -> bool:
    if user == "Nikita":
        print("True")
        return True
    else:
        print("False")
        return False
    

user_check_name(user=user)