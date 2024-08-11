import prompt
import random


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
        correct_answer = 'yes'
        return question, correct_answer
    else:
        correct_answer = 'no'
        return question, correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(3):
        question, correct_answer = get_question()
        print(question)
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
        print("Correct")

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
