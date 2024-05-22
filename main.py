import logging
import random

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.INFO, format='[%(asctime)s] [%(levelname)s] [%(message)s]')


def log_message(role, message):
    logging.info(f"[{role}]: {message}")


def main():
    number_to_guess = random.randint(1, 100)
    log_message("System", f"Загадано число {number_to_guess}")

    attempts = 0
    attempts_limit = 10
    numbers_greater = []
    numbers_less = []

    while attempts < attempts_limit:
        try:
            user_input = input("Введите ваше число: ")
            guess = int(user_input)
            attempts += 1
            log_message("User", f"Введено число {guess}")

            if guess < number_to_guess:
                print("Загаданное число больше.")
                numbers_less.append(guess)
            elif guess > number_to_guess:
                print("Загаданное число меньше.")
                numbers_greater.append(guess)
            else:
                print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
                log_message("System", "Число угадано.")
                log_message("System", f"Попыток: {attempts}")
                break

        except ValueError:
            print("Ошибка: введите корректное число.")
            log_message("System", "Ошибка ввода: не числовое значение.")

    else:
        print(f"Вы исчерпали {attempts_limit} попыток. Загаданное число было {number_to_guess}.")
        log_message("System", f"Попытки исчерпаны. Загаданное число было {number_to_guess}.")

    log_message("System", f"Числа больше загаданного: {numbers_greater}")
    log_message("System", f"Числа меньше загаданного: {numbers_less}")


if __name__ == "__main__":
    main()
