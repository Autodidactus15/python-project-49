import random
import prompt


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name
    print(f'Hello, {name}!')



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question():
    number = random.randint(1, 100)
    question = f'{number}'

    if is_prime(number):
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, str(answer)
