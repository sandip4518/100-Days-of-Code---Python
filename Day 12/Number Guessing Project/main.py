import os

import art
import random

def guess_number():
    os.system('cls')
    def reset():
        ch=input("\nRestart(r) or Exit(e) : ").lower()
        if ch=='r':
            os.system('cls')
            guess_number()
        else:
            print("You have exited the game!")
            exit()
    print("\n")
    print(art.logo)
    print("Welcome to the number guessing game!😊")
    print("I am thinking of an number between 1 to 100.")
    choice = input("Choose the difficulty.Easy(e) or hard(h): ").lower()
    random_number = int(random.randint(0, 100))

    if choice == 'e':
        attempts = 10
        while attempts:
            print(f"\nYou have {attempts} remaining to guess the number.")
            guess = int(input("Guess the number : "))
            if guess == random_number:
                print(f"Got it! number is {random_number}.")
                reset()
            elif guess > random_number:
                print("Too high.\nSorry Guess Again!")
            else:
                print("Too low.\nSorry Guess Again!")
            attempts -= 1
        print(f"You Lost! number is {random_number}.")
        reset()
    else:
        attempts = 5
        while attempts:
            print(f"\nYou have {attempts} remaining to guess the number.")
            guess = int(input("Guess the number : "))
            if guess == random_number:
                print(f"Got it! number is {random_number}")
                reset()
            elif guess > random_number:
                print("Too high.\nSorry Guess Again!")
            else:
                print("Too low.\nSorry Guess Again!")
            attempts -= 1
        print(f"You Lost! number is {random_number}.")
        reset()

guess_number()