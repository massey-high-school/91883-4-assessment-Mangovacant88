# component uno

# To Do
# generate addition question
# generate 2 numbers for each question
# check number is between 0 and 50

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

