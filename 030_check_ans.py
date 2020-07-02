# Generate a random number between 0 and 50

# to do
# import 2 random numbers between 0 and 50

# import random numbers

import random
# import random numbers

# variables
low = 0
high =  50
guess = ""


NuQuestion = random.randint(low, high)
# print(NuQuestion)
NuQuestion02 = random.randint(low, high)
# print(NuQuestion, NuQuestion02, end="\t")

question = "{} + {}".format(NuQuestion, NuQuestion02)
print(question)

Answer = NuQuestion + NuQuestion02

guess = int(input("Enter the answer here:"))

if guess == Answer:
    print("nice my bro you got it correct!!")
else:
    print("bruhh you got it wrong you needa work on your addition questions")