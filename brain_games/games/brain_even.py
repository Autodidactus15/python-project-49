import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 1000
MIN_NUMBER = 1


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{number}"

    if is_even(number):
        answer = 'yes'
        return question, str(answer)
    else:
        answer = 'no'
        return question, str(answer)
