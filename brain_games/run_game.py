import prompt


ATTEMPTS_COUNT = 3


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = say_hello()
    print(game.RULE)
    for i in range(ATTEMPTS_COUNT):
        question, answer = game.get_question()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")

        if user_answer == answer:
            print("Correct")
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
