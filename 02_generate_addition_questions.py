import random

# import random numbers

# variables
low = 0
high = 50
guess_the_question = ""

NuQuestion = random.randint(low, high)
# print(NuQuestion)
NuQuestion02 = random.randint(low, high)
# print(NuQuestion, NuQuestion02, end="\t")

question = "{} + {}".format(NuQuestion, NuQuestion02)
print(question)

Answer = NuQuestion + NuQuestion02

guess_the_question = int(input("Enter the answer here:"))

if guess_the_question == Answer:
    print("nice you got it correct!!")
else:
    print("sorry you got it wrong")
