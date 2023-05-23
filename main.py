# TODO: IMPORTS
from art import logo
from random import randint
import os

def clear():
  return os.system('clear')


def guess_number():
    easy = 10
    hard = 5
    still = True

    print(f"{logo}\nWelcome to the Number Guessing Game!\nI am thinking on a number between 1 and 100.\n")
    secret_number = randint(1, 101)

    # print(f"Help --- > the number is {secret_number}")
    level = input("Chose a difficulty, easy or hard:\n")

    if level == "easy":
        lives = easy
    else:
        lives = hard

    while still:
        if lives == 1:
            print("Last chance!!")
        if lives > 0:
            print(f"You have {lives} attempts remaining to guess my number ")
            guess = int(input("Make a guess:\n"))
            if guess < secret_number:
                print("Too low, you lose a life")
                lives -= 1
            elif guess > secret_number:
                print("Too high, you lose a life")
                lives -= 1
            else:
                still = False
                print(f"You guessed the number! it was {secret_number}!!!!")
        else:
            still = False
            print(f"You did not guess the number! it was {secret_number}!!!!")

while input("Do you want to play? 'y' or 'n'") == "y":
    clear()
    guess_number()
