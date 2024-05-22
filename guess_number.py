import random


def generate_number():
    return random.randint(1, 100)


def check_guess(guess, number):
    if guess < number:
        return "less"
    elif guess > number:
        return "greater"
    else:
        return "equal"
