import prompt
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string("Your answer: ")

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer != correct_answer:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
        print("Correct")

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
