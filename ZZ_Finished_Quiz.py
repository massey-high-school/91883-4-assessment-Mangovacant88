
# Number checker function goes here
def intcheck(question, low, high):
    valid = False
    error = "oops, please put in a number between {} and {}".format(low, high,)
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

# main routine goes here

how_much = intcheck("how many questions would you like to answer? ", 1, 10)
print("You have chosen to answer {} questions".format(how_much))


# import random numbers

import random

low = 0
high = 50


NuQuestion = random.randint(low, high)
print(NuQuestion)
NuQuestion02 = random.randint(low, high)
print(NuQuestion, NuQuestion02, end="\t")

question = "{} + {}".format(NuQuestion, NuQuestion02)
print(question)

# import random numbers

import random

low = 0
high = 50

for item in range(1, 2):
    NuQuestion = random.randint(low, high)
    NuQuestion02 = random.randint(low, high)

    question = "{} + {}".format(NuQuestion, NuQuestion02)
    answer = NuQuestion + NuQuestion02

    question = input("Enter the answer here:")

