import random

EASY = 10
HARD = 5

def attempt(num, answer):


print("Welcome to the number guesser game!")
print("I'm thinking of a number between 1 and 100 inclusive, your job is to guess it. Ready?")
user_choice = input("Choose the easy or hard mode: E/H").lower()

if user_choice == "e":
    for n in range(1,11):
        attempt()
if user_choice == "h":
    for n in range(1,6):
        attempt()