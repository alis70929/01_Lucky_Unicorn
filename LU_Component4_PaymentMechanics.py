# Lucky Unicorn Component 4
# Payment mechanics

#assume starting amount is $10
total = 10

#Allow manual input of token for testing
token = input("Which token would you like?:")

#Adjust total correctly for given token
if token == "unicorn":
    total += 5
    feedback = "Lucky, You won $5.00 "
elif token == "donkey":
    total -= 1
    feedback = "Unlucky, you won nothing"
else:
    total += 0.5
    feedback = "Nice, you won $0.50"
print()

print(feedback)
print("You have ${:.2f} to play with".format(total))

