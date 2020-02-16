#Lucky Unicorn Full Program

import random

#Functions go here

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

# Ask User how much they want to play with (min $1 max $10)
balance = intcheck("How much money would you like to play with between {} - {}",1,10)

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
        feedback = "Congratulations, You won $5.00 "
    elif chosen_token == "donkey":
        balance -= 1 # Does not win anything (ie: loses $1)
        feedback = "Sorry, you won nothing"
    else:
        balance -= 0.5 # 'Wins' 50c, paid 1 dollar so loses 50c
        feedback = "Congratulations, you won $0.50"
    print()
    # Display feedback and current balance
    print(feedback)
    print("You have ${:.2f} to play with".format(balance))

    # If user has eneough money ask them if they want to keep playing. If they do not have enough money end the game
    if balance < 1:
        print("Sorry, you dont have enough money to continue. Game Over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play agin or any key to quit ")

print("Thank you for playing")
print("You have ended with ${:.2f}".format(balance))