import random


def multiply(number_1, number_2):
    return number_1 * number_2


def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    random_operation = random.choice((multiply, subtract, sum_numbers))

    if random_operation == multiply:
        question = f"Question: {number_1} * {number_2}"
        answer = multiply(number_1, number_2)
        return question, answer
    elif random_operation == subtract:
        question = f"Question: {number_1} - {number_2}"
        answer = subtract(number_1, number_2)
        return question, answer
    elif random_operation == sum_numbers:
        question = f"Question: {number_1} + {number_2}"
        answer = sum_numbers(number_1, number_2)
        return question, answer
