import prompt
import random


def get_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'Question: {number_1} {number_2}'

    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
    else:
        answer = number_1
        return question, answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")

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
