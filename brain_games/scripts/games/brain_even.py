import random
import prompt


def question():
    number = random.randint(1, 1000)
    print(f"Question: {number}")

    if number % 2 == 0:
        answer = 'yes'
        return answer
    else:
        answer = 'no'
        return answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        answer = question()
        user_answer = input("Your answer: ")

        if user_answer == answer:
            print("Correct")
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
