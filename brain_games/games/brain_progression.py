import random


RULE = "What number is missing in the progression?"
MAX_NUMBER = 100
MIN_NUMBER = 1
MIN_STEP = 1
MAX_STEP = 5
MIN_NUMBER_POSITION = 0
MAX_NUMBER_POSITION = 7


def progression(start_point, step):
    length = 10
    progression_list = []
    while length != 0:
        progression_list.append(start_point + step)
        length -= 1
        start_point += step
    return progression_list


def get_question():
    start_point = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    missing_number = random.randint(MIN_NUMBER_POSITION, MAX_NUMBER_POSITION)

    progression_set = progression(start_point, step)
    old_progression_set = progression_set.copy()
    answer = old_progression_set[missing_number]
    progression_set[missing_number] = ".."
    question = (" ".join(list(map(str, progression_set))))
    return question, str(answer)
