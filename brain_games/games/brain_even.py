import random


def get_question():
    number = random.randint(1, 1000)
    question = f"Question: {number}"

    if number % 2 == 0:
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, answer
