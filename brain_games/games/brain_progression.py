import random
import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")


def progression(number_1, number_2):
    length = 10
    progression_list = []
    while length != 0:
        progression_list.append(number_1 + number_2)
        length -= 1
        number_1 += number_2
    return progression_list


def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 5)
    number_3 = random.randint(0, 7)

    pr_list = progression(number_1, number_2)
    old_pr_list = pr_list.copy()
    answer = old_pr_list[number_3]
    pr_list[number_3] = ".."
    question = (f'Question: {pr_list[0]} {pr_list[1]} '
                f'{pr_list[2]} {pr_list[3]} {pr_list[4]} '
                f'{pr_list[5]} {pr_list[6]} {pr_list[7]}')
    return question, answer
