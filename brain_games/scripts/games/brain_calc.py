import random
import prompt


def multiply(number_1, number_2):
    """Return the product of two numbers."""
    return number_1 * number_2


def sum_numbers(number_1, number_2):
    """Return the sum of two numbers."""
    return number_1 + number_2


def subtract(number_1, number_2):
    """Return the difference of two numbers."""
    return number_1 - number_2


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    
    counter = 0
    while counter < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        random_operation = random.choice((multiply, subtract, sum_numbers))
        
        if random_operation == multiply:
            print(f"Question: {number_1} * {number_2}")
            answer = multiply(number_1, number_2)
        elif random_operation == subtract:
            print(f"Question: {number_1} - {number_2}")
            answer = subtract(number_1, number_2)
        else:
            print(f"Question: {number_1} + {number_2}")
            answer = sum_numbers(number_1, number_2)
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

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
