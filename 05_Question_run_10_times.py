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

for item in range(1, 10):
    question2 = random.randint(low, high)

    NuQuestion = random.randint(low, high)
    # print(NuQuestion)
    NuQuestion02 = random.randint(low, high)
    # print(NuQuestion, NuQuestion02, end="\t")

    question = "{} + {}".format(NuQuestion, NuQuestion02)
    print(question)

    Answer = NuQuestion + NuQuestion02

    guess = int_check("Enter the answer here:", low, high)

    if guess == Answer:
        print("nice you got it correct!!")
    else:
        print("sorry you got it wrong")
