import random
import math


RULE = "Find the greatest common divisor of given numbers."
MAX_NUMBER = 100
MIN_NUMBER = 1


def get_question():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_number} {second_number}'

    answer = math.gcd(first_number, second_number)
    return question, str(answer)
