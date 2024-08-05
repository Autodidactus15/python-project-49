import prompt
import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    counter = 0
    while counter < 3:
        number_1 = random.randint(1, 100)
        print(f'Question: {number_1}')
        
        if is_prime(number_1):
            answer = "yes"
        else:
            answer = "no"
        
        user_answer = input("Your answer: ")
        
        if not user_answer.isalpha():
            print('Please, insert "yes" or "no"')
            break
        
        user_answer = user_answer.lower()
        
        if user_answer == answer:
            print("Correct")
            counter += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

