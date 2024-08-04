import prompt 
import random

def progression(number_1, number_2):
    length = 10
    progression_list = []
    while length != 0: 
        progression_list.append(number_1 + number_2)
        length -= 1
        number_1 += number_2
    return progression_list



def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")
    counter = 0 
    while counter < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 5)
        number_3 = random.randint(0, 9)
        pr_list = progression(number_1, number_2)
        old_pr_list = pr_list.copy()
        answer = old_pr_list[number_3]
        pr_list[number_3] = ".."   
        print(f'Question: {pr_list[0]} {pr_list[1]} {pr_list[2]} {pr_list[3]} {pr_list[4]} {pr_list[5]} {pr_list[6]} {pr_list[7]} {pr_list[8]} {pr_list[9]}')
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
