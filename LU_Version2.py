#Lucky Unicorn Full Program

import random

#Functions go here

# Makes the token statements look good.
def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()
# Integer checking function
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

# Introduction
print("------ Lucky Unicorn ------")
print()
print("To play, enter an amount of money between $1 and $10 (Whole dollars only)")
print()
print("- It costs $1/round")
print()
print("Payouts...")
print("- Unicorn: $5")
print("- Horse/Zebra: $0.5")
print("- Donkey: $0")
print("")

# Ask User how much they want to play with (min $1 max $10)
balance = intcheck("How much money would you like to play with between ${:.2f} - ${:.2f}: ",1,10)

keep_going = ""
while keep_going == "":

    # Token list includes 10 items to make sure not too many unicorns are chosen
    tokens =["horse","horse","horse",
             "zebra","zebra","zebra",
             "donkey","donkey","donkey","unicorn"]

    # randomly choose and display a token
    chosen_token = random.choice(tokens)
    print()
    print("You got a {}".format(chosen_token))

    # Adjust balance based on chosen token and generate feedback
    if chosen_token == "unicorn":
        balance += 5 # Wins 5 dollars
        # Unicorn token statement
        token_statement("*** Congratz,You got a unicorn. You won $5 ***","*")
    elif chosen_token == "donkey":
        balance -= 1 # Does not win anything (ie: loses $1)
        # Donkey token statement
        token_statement("--- You got a donkey, you win nothing ---","-")
    else:
        balance -= 0.5 # 'Wins' 50c, paid 1 dollar so loses 50c
        # Zebra and horse token statement
        token_statement("^^^ You got a {}, you won back $0.50 ^^^".format(chosen_token),"^")
    print()
    # Display current balance
    print()
    print("You have ${:.2f} to play with".format(balance))
    print()

    # If user has eneough money ask them if they want to keep playing. If they do not have enough money end the game
    if balance < 1:
        print("Sorry, you dont have enough money to continue. Game Over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play agin or any key to quit ")

print("Thank you for playing")
print("You have ended with ${:.2f}".format(balance))