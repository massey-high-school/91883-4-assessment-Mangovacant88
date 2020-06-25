# Generate a random number between 0 and 50

# to do
# import 2 random numbers between 0 and 50

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





