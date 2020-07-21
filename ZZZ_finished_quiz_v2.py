print()
print("************************************")
print("welcome to the Amazing Addition Quiz")
print("************************************")
print()

# Number checker function goes here
def int_check(question, low, high):
    valid = False
    error = "Error, please put in something between {} and {}".format(low, high,)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
# main routine

# import random numbers

# variables
import random


low = 0
high =  100

for item in range(1, 4):
    question2 = random.randint(low, high)

    NuQuestion = random.randint(low, high)
    # print(NuQuestion)
    NuQuestion02 = random.randint(low, high)
    # print(NuQuestion, NuQuestion02, end="\t")

    question = "{} + {}".format(NuQuestion, NuQuestion02)
    print(question)

    Answer = NuQuestion + NuQuestion02

    guess = int_check("Enter the answer here:", low, 200)

    if guess == Answer:
        print("nice you got it correct!!")
    else:
        print("sorry you got it wrong")

# print quiz outcomes...
import random

how_many_questions = 3
correct = 0
wrong = 0

result = ""

game_history = []

print()
print("*****The best game ever*****")
print("Type in 'correct' if you got it correct, or anything else if you got it wrong")
print()

for item in range(1, how_many_questions + 1):

    result = input("Game Result? ")

    if result == "correct":
        feedback = "you got it correct"
        correct += 1
    else:
        feedback = "Sorry you got it wrong"
        wrong += 1

    round_result = "Round {}: {}".format(item, feedback)
    game_history.append(round_result)

print()
print("***** Results *****")

for item in game_history:
    print(item)

print()
print("**********************************************")
print("Thanks for answering The Amazing Addition Quiz")
print("**********************************************")
print()