# Import logos and modules
import random
import art
# print(art.logo)
# print(art.vs)

import game_data
# print(len(game_data.data))

# Function - retrieves a random pair of people from the dictionary,
# does a comparison on their follower count and outputs the correct answer (higher count)

def get_pair(index1, index2):
    correct_answer = ""
    personAcount = game_data.data[index1]['follower_count']
    personBcount = game_data.data[index2]['follower_count']

    if personAcount > personBcount:
        correct_answer = "A"
    else:
        correct_answer = "B"

    return correct_answer

# Function - prompts user to guess which of the random pair is correct, compares input to answer, and sets flag True/False
def compare_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        global score += 1
    else:
        global flag = False
        # It should only declare a variable, not modify it in the same line. You cannot use global and modify a variable like global score += 1. Instead, declare the variables globally outside the functions.
        # You should declare the variable flag as a global variable if you intend to modify it inside the function.
    return score

# Function / Main program - while True (user is correct), loop the 2 functions, otherwise terminate game and provide final scope

def main():
        flag = True
        score = 0

        while flag = True:
            index1 = random.randint(1,len(game_data.data)) # Randint is inclusive of both start/stop values
            index2 = index1 + 1
            user_answer = input("Who has more followers? A or B? >>").upper()
            get_pair(index1, index2)
            compare_answer(user_answer, correct_answer)

            print(art.logo)
            print(f"Compare A: {game_data.data[index1]['name']}, a {game_data.data[index1]['description']}, from {game_data.data[index1]['country']}.")
            print(art.vs)
            print(f"against B: {game_data.data[index2]['name']}, a {game_data.data[index2]['description']}, from {game_data.data[index2]['country']}.")

        if flag = True:
            print(f"You're right! Score so far {score}. Keep going!")
        if flag = False:
            print(f"You're wrong, sorry. Final scope: {score}")