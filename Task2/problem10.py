import time
import random
def check_int(n):
    try:
        n = int(n)
    except:
        n = input("Enter an integer this time: ")
        n = check_int(n)
    return n
def check_include(n):
    while True:
        if n < 1 or n > 100:
            n = check_int(input("The guess is between 1 and 100! pay attention & try again: "))
            continue
        break
    return n
for _ in range(50):
    print("=",end="")
    time.sleep(0.1)
print()
time.sleep(0.5)
print("                   Guess Game                        ")
time.sleep(0.5)
option = "y"
while option.lower() == "y":
    num = random.randint(1, 100)
    guess = input("guess a number between 1 and 100: ")
    while True:
        guess = check_include(check_int(guess))
        if guess < num:
            guess = input("Guess is too low: ")
        elif guess > num:
            guess = input("Guess is too high: ")
        else:
            print("Oh yessss! you guessed it right!\nGongrats you won!")
            option = input("Wanna play again?(y/n): ")
            if option.lower() == "n":
                print("Thank you for playing <3.")
                time.sleep(1)
                print("======================= Game over =======================")
                time.sleep(1)
            break
                
