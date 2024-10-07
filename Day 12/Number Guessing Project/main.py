# import random
#
# EASY = 10
# HARD = 5
#
# answer = random.randint(1,100)
# user_guess = ""
# attempts_left = 0
#
# def attempt(user_guess, answer, attempts_left):
#     user_guess = int(input("Make a guess:")) # Must be integer
#
#     if user_guess > answer:
#         print("Too high")
#         print("Guess again.")
#         print(f"You have {attempts_left} attempts remaining to guess the number.")
#
#     elif user_guess < answer:
#         print("Too low.")
#         print("Guess again.")
#         print(f"You have {attempts_left} attempts remaining to guess the number.")
#
#     elif user_guess == answer:
#         print("You won!")
#         return
#
# print("Welcome to the number guesser game!")
# print("I'm thinking of a number between 1 and 100 inclusive, your job is to guess it. Ready?")
# user_choice = input("Choose the easy or hard mode: E/H").lower()
#
# if user_choice == "e":
#     attempts_left = EASY
#     for n in range(1,11):
#         attempts_left -= 1
#         attempt(user_guess, answer)
#
# if user_choice == "h":
#     attempts_left = HARD
#     for n in range(1,6):
#         attempt(user_guess, answer)

# CORRECTED CODE BELOW
import random

EASY = 10
HARD = 5

answer = random.randint(1, 100)


def attempt(user_guess, answer, attempts_left):
    """Handle the user's guess and return remaining attempts."""
    user_guess = int(input("Make a guess: "))  # Must be integer

    if user_guess > answer:
        print("Too high.")
    elif user_guess < answer:
        print("Too low.")
    else:
        print(f"Congratulations! You've guessed the number {answer} correctly!")
        return attempts_left  # Returning to stop further guesses

    # Reduce attempts after each wrong guess
    attempts_left -= 1
    print(f"You have {attempts_left} attempts remaining.")

    return attempts_left


def play_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100 inclusive. Your job is to guess it. Ready?")

    user_choice = input("Choose a mode: 'E' for easy or 'H' for hard: ").lower()

    # Set number of attempts based on mode
    if user_choice == "e":
        attempts_left = EASY
    elif user_choice == "h":
        attempts_left = HARD
    else:
        print("Invalid choice! Please select 'E' for easy or 'H' for hard.")
        return

    # Loop until the user runs out of attempts or guesses the correct answer
    while attempts_left > 0:
        attempts_left = attempt(user_guess=None, answer=answer, attempts_left=attempts_left)

        # If attempts_left is not returned (meaning the user won), break the loop
        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The correct number was {answer}.")
            break


# Start the game
play_game()