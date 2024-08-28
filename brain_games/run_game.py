import prompt


ATTEMPTS = 3


def run_game(game):
    name = game.say_hello()
    print(game.RULE)
    for i in range(ATTEMPTS):
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
