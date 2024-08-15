import random
import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question():
    number = random.randint(1, 1000)
    question = f"Question: {number}"

    if number % 2 == 0:
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, answer
