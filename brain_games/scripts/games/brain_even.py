import random
import prompt


def get_question():
    number = random.randint(1, 1000)
    question = f"Question: {number}"

    if number % 2 == 0:
        answer = 'yes'
        return question, answer
    else:
        answer = 'no'
        return question, answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        question, answer = get_question()
        print(question)
        user_answer = prompt.string("Your answer: ")

        if user_answer == answer:
            print("Correct")
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
