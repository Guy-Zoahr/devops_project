from random import randint

difficulty = 5


def generate_number():
    secret_number = randint(1, difficulty)


def get_guess_from_user():
    user_guessed_number = input("pick number between 1 and {}".format(difficulty))
    return user_guessed_number


def compare_results(secret_number, user_number):
    if secret_number == user_number:
        return True
    else:
        return False
