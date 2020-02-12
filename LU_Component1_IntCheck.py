#Lucky Unicorn Component 1 IntCheck
# Loops question so it repeats until a valid number is entered
# make code recyclable

#Functions go here
def intcheck(question,low,high):
    valid = False
    error = "Whoops, please enter an integer between {} - {}".format(low,high)
    while not valid:
        try:
            response = int(input(question.format(low,high)))
            if low <= response <= high:
                return response
                valid = True
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()
#Main routine goes here
how_much = intcheck("How much money would you like to play with between {} - {}",1,10)
