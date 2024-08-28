import random
import prompt


RULE = "Find the greatest common divisor of given numbers."


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name
    print(f'Hello, {name}!')



def get_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'

    while second_number != 0:
        first_number, second_number = second_number, first_number % second_number
    else:
        answer = first_number
        return question, str(answer)
