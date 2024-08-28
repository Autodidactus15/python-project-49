import random
import prompt


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_question():
    number = random.randint(1, 1000)
    question = f"{number}"

    if number % 2 == 0:
        answer = 'yes'
        return question, str(answer)
    else:
        answer = 'no'
        return question, str(answer)
