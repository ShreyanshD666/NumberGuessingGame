import random

print("Number Guessing: The Game")

number = random.randint(1, 9)
chances = 0

print("Guess A Number (Between 1 and 9): ")

while chances < 5:

    guess = int(input("Enter Your Guess: "))

    if guess == number:
        print("Great Job, You Won!")
        break

    elif guess < number:
        print("Your Guess Was Too Low, Guess A Number Higher Than: ", guess)

    else:
        print("Your Guess Was Too High, Guess A Number Lower Than: ", guess)
    
    chances = chances + 1

if not chances < 5:
    print("Oh No, You Lost - The Number Is: ", number)

    
