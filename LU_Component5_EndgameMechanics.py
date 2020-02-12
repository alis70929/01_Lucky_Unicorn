# Lucky Unicorn Component 4
# Payment mechanics

#assume starting amount is $10
total = int(input("How much would you like to play with: "))

#Allow manual input of token for testing
token = input("Which token would you like?: ")

keepgoing = ""
while keepgoing == "":
    #Adjust total correctly for given token
    if token == "unicorn":
        total += 5
        feedback = "Lucky, You won $5.00 "
    elif token == "donkey":
        total -= 1
        feedback = "Unlucky, you won nothing"
    else:
        total += 0.5
        feedback = "meh, you won $0.5"
    print()

    print(feedback)
    print("You have ${:.2f} to play with".format(total))

    if total < 1:
        print("Sorry, you dont have enough money to continue. Game Over")
