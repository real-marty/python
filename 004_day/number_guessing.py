

import random
print("Welcome to the number guessing game")


def game_setup(dificulty):
    if dificulty == "easy":
        attempts = 10
        max_number = 100
        print("You have 10 attempts to guess a number between 1 and 100")
    elif dificulty == "medium":
        attempts = 7
        max_number = 150
        print("You have 7 attempts to guess a number between 1 and 150")
    elif dificulty == "hard":
        attempts = 5
        max_number = 200
        print("You have 5 attempts to guess a number between 1 and 200")
    else:
        print("Invalid input")
    return attempts, max_number


while True:
    print("Choose a dificulty: easy, medium, hard")
    dificulty = input()
    attempts, max_number = game_setup(dificulty)
    if attempts == None or max_number == None:
        continue
    number = random.randint(1, max_number)
    while attempts > 0:
        print(f"You have {attempts} attempts left")
        print("Guess the number")
        guess = int(input())
        if guess == number:
            print("You won")
            break
        elif guess > number:
            print("Too high")
        else:
            print("Too low")
        attempts -= 1
    if attempts == 0:
        print("You lost")
        print(f"The number was {number}")
    print("Do you want to play again? (y/n)")
    cont = input()
    if cont == "n":
        break
    elif cont == "y":
        continue
    else:
        print("Invalid input")
    
