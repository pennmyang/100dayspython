# Functions with input

# def greet_with_name(name,location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")
#
#
# # greet_with_name("Jack Bauer","macdonalds")
# greet_with_name(location="maccy Ds",name="Jack Bauer")

def calculate_love_score(name1,name2):
    combinedName = name1 + name2

    totalOne = 0
    totalTwo = 0

    wordOne = "TRUE"
    wordTwo = "LOVE"

    for letter in combinedName.upper():
        if letter in wordOne:
            totalOne +=1


    for letter in combinedName.upper():
        if letter in wordTwo:
            totalTwo +=1


    print(f"{totalOne}{totalTwo}")

calculate_love_score("mick","nicole")

calculate_love_score("benny mango boom","dango wango")