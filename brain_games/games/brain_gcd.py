import random
import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")


def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'Question: {number_1} {number_2}'

    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
    else:
        answer = number_1
        return question, answer
