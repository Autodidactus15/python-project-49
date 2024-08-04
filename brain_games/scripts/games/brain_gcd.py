import prompt 
import random

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")
    counter = 0 
    while counter < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        while number_2 != 0:
            number_1, number_2 = number_2, number_1 % number_2
        else:
            answer = number_1
        user_answer = input("Your answer: ")
        if user_answer.isalpha():
           print("Please, insert a number")
           break
        user_answer = int(user_answer)
        if user_answer == int(answer):
            print("Correct")
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer} .")
            print(f"Let's try again, {name}!")
            break  
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
