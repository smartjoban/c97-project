import random

number = random.randint(1,9)
chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("Enter your guess:- "))

    if number == guess:
        print("Congratulations" )
        break

    elif guess < number: 
        print("Your Guess Was Too Low")    

    else:
        print("Your Guess Was Too High")    

    chances = chances +1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)