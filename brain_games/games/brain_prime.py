import random
import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question():
    number = random.randint(1, 100)
    question = f'Question: {number}'

    if is_prime(number):
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, answer
