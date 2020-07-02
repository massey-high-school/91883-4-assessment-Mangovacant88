import random

# number checking function goes here
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

# Main routine goes here



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
