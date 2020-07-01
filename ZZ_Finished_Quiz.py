import random

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

# import random numbers

low = 0
high = 50
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
    print("correct!")
else:
    print("You got it wrong")
