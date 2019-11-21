import time
import random
def decide_number():
    for i in range(1):
        return(random.randint(1,6))
def perform_judge(y1, y2):
    if y1>y2:
        print("You lose!")
    elif y1==y2:
        print("Draw!")
    else:
        print("You win!")
def main():
    random.seed(time.time())
    play_again = 'y'
    while play_again == 'y':
        comp = decide_number() + decide_number()
        print("The sum of my result is {}!".format(comp))
        input ("Press any key to roll the first one.")
        value1 = decide_number()
        print("Your first result is {}".format(value1))
        input ("Press any key to roll the second one.")
        value2 = decide_number()
        print("Your second result is {}".format(value2))
        total_result = value1 + value2
        print("Total number of your result is {}!".format(total_result))
        perform_judge(comp, total_result)
        play_again = input("Wanna play again? (y/n)")
main()
