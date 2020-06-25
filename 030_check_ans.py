# Generate a random number between 0 and 50

# to do
# import 2 random numbers between 0 and 50

# import random numbers

import random

low = 0
high = 50
Answer = (low + high)
guess = ""

for item in range (1,2):
    NuQuestion = random.randint(low, high)
    NuQuestion02 = random.randint(low, high)


    question = "{} + {}".format(NuQuestion, NuQuestion02)
    answer = NuQuestion + NuQuestion02


    guess = int(input("Enter the answer here:")

    if guess - Answer:
        print("Wrong")
    else:
        print("Nice you got it correct!")


