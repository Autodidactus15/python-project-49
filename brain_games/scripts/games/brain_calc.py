import random
import prompt 

def multiply(number_1, number_2):
    return number_1 * number_2
def sum(number_1, number_2):
    return number_1 + number_2
def substract(number_1, number_2):
    return number_1 - number_2
def divide(number_1, number_2):
    return number_1 + number_2
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    counter = 0 
    while counter < 3:
       number_1 = random.randint(1, 100)
       number_2 = random.randint(1, 100)
       random_operation = random.choice((multiply, substract, sum))
       if random_operation == multiply:
          print(f"Question: {number_1} * {number_2} ")
          answer = number_1 * number_2
       elif random_operation == substract:
          print(f'Question: {number_1} - {number_2} ')
          answer = number_1 - number_2
       else:
          print(f'Question: {number_1} + {number_2} ')
          answer = number_1 + number_2
       if user_answer.isalpha():
           print("Please, insert a number")
           break
       user_answer = int(user_answer)
       if user_answer == int(answer):
            print("Correct")
            counter += 1
       else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer} .")
            print(f"Let's try again, {name}")
            break  
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
