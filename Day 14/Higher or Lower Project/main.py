# ChatGPT version of code - I progressed! While I didn't know how to sequence and scope my while loop,
# this time I knew there were 3 functions to create and the arguments to pass into them.

# Import logos and modules
import random
import art
import game_data

# Initialize global variables for score and flag
score = 0
flag = True

# Function - retrieves a random pair of people from the dictionary, compares their follower count
def get_pair(index1, index2):
    personAcount = game_data.data[index1]['follower_count']
    personBcount = game_data.data[index2]['follower_count']

    if personAcount > personBcount:
        return "A"
    else:
        return "B"
    # note didn't need to store A or B into a correct_answer variable

# Function - compares user input to the correct answer and updates score or flag
def compare_answer(user_answer, correct_answer):
    global score, flag # creating local copies of global variables - you should only declare a variable, not modify it in the same line.
    if user_answer == correct_answer:
        score += 1 # modifying happens separately
        print(f"You're right! Score so far {score}. Keep going!")
    else:
        flag = False
        print(f"You're wrong, sorry. Final score: {score}")

# Main function
def main():
    global flag
    flag = True

    while flag:  # Comparison, not assignment - loop condition that checks the truthiness, so this means "keep looping as long as flag is True."
        index1 = random.randint(0, len(game_data.data) - 2)  # Avoid out-of-range error, but flaw is that 50th dictionary will never be used.
        # 2 alternative ways:
        # (1) randomly select two distinct indices (index1 and index2) and compare their follower counts -> for both, use random.randint(0, len(game_data.data) - 1), and have another while check to make sure they're distinct
        # (2) shuffle the list and then take adjacent pairs for comparison, ensuring randomness without worrying about index boundaries.
                # indices = list(range(len(game_data.data)))
                # random.shuffle(indices)
                #
                # index1 = indices[0]
                # index2 = indices[1]

        index2 = index1 + 1

        # Print the details of person A and person B before asking for input
        print(art.logo)
        print(f"Compare A: {game_data.data[index1]['name']}, a {game_data.data[index1]['description']}, from {game_data.data[index1]['country']}.")
        print(art.vs)
        print(f"Against B: {game_data.data[index2]['name']}, a {game_data.data[index2]['description']}, from {game_data.data[index2]['country']}.")

        # Ask for the user's guess
        user_answer = input("Who has more followers? A or B? >> ").upper()

        # Get the correct answer and compare it
        correct_answer = get_pair(index1, index2)
        compare_answer(user_answer, correct_answer)

# Run the game
main()
