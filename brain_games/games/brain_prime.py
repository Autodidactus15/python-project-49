import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number}'

    if is_prime(number):
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, str(answer)
