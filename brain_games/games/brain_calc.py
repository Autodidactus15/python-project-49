import random


RULE = "What is the result of the expression?"
MAX_NUMBER = 100
MIN_NUMBER = 1


def multiply(first_number, second_number):
    return first_number * second_number


def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def get_question():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_operation = random.choice((multiply, subtract, sum_numbers))

    if random_operation == multiply:
        question = f"{first_number} * {second_number}"
        answer = multiply(first_number, second_number)
        return question, str(answer)
    elif random_operation == subtract:
        question = f"{first_number} - {second_number}"
        answer = subtract(first_number, second_number)
        return question, str(answer)
    elif random_operation == sum_numbers:
        question = f"{first_number} + {second_number}"
        answer = sum_numbers(first_number, second_number)
        return question, str(answer)
