import prompt
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def question():
    number = random.randint(1, 100)
    print(f'Question: {number}')

    if is_prime(number):
        correct_answer = 'yes'
        return correct_answer
    else:
        correct_answer = 'no'
        return correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 0
    while counter < 3:
        correct_answer = question()
        user_answer = input()

        if user_answer != correct_answer:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
        print("Correct")

        counter += 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
