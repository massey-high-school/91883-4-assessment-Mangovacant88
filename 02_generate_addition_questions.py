# Generate a random number between 0 and 50

# to do
# import 2 random numbers

# import random numbers

import random

low = 0
high = 50

for item in range(low, high):
    secret = random.randint(low, high)
    print(secret, end="\t")


