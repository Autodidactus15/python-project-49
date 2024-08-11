import random
import prompt


def multiply(number_1, number_2):
    return number_1 * number_2


def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    random_operation = random.choice((multiply, subtract, sum_numbers))

    if random_operation == multiply:
        question = f"Question: {number_1} * {number_2}"
        answer = multiply(number_1, number_2)
        return question, answer
    elif random_operation == subtract:
        question = f"Question: {number_1} - {number_2}"
        answer = subtract(number_1, number_2)
        return question, answer
    elif random_operation == sum_numbers:
        question = f"Question: {number_1} + {number_2}"
        answer = sum_numbers(number_1, number_2)
        return question, answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")

    for i in range(3):
        question, answer = get_question()
        print(question)
        user_answer = prompt.integer("Your answer: ")

        if user_answer == answer:
            print("Correct")
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
