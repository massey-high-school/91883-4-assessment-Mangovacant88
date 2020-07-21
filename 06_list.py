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

