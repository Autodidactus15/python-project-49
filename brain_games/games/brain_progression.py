import random
import prompt


RULE = "What number is missing in the progression?"


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def progression(start_point, step):
    length = 10
    progression_list = []
    while length != 0:
        progression_list.append(start_point + step)
        length -= 1
        start_point += step
    return progression_list


def get_question():
    start_point = random.randint(1, 100)
    step = random.randint(1, 5)
    missing_number = random.randint(0, 7)

    progression_set = progression(start_point, step)
    old_progression_set = progression_set.copy()
    answer = old_progression_set[missing_number]
    progression_set[missing_number] = ".."
    question = (" ".join(list(map(str, progression_set))))
    return question, str(answer)
