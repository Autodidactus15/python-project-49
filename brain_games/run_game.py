import prompt


def run_game(game):
    game.say_hello()
    for i in range(3):
        question, answer = game.get_question()
        print(question)
        if isinstance(answer, int):
            user_answer = prompt.integer("Your answer: ")
        else:
            user_answer = prompt.string("Your answer: ")

        if user_answer == answer:
            print("Correct")
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {answer}.")
            print(f"Let's try again, {game.name}!")
            break
    else:
        print(f'Congratulations, {game.name}!')
