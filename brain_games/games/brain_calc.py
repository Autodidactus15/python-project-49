import random
import prompt


RULE = "What is the result of the expression?"


def multiply(first_number, second_number):
    return first_number * second_number


def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name
    print(f'Hello, {name}!')


def get_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
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
