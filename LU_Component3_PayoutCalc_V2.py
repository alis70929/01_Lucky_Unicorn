#Lucky Unicorn Component 3
#Generate a random token

import random
HOW_MUCH = 100

tokens =["horse","horse","horse",
         "zebra","zebra","zebra",
         "donkey","donkey","donkey","unicorn"]

unicorn_count = 0
zebhor_count = 0
donkey_count = 0
for item in range(0,HOW_MUCH):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebhor_count += 1

    print(chosen)
#Money Claculations
winnings = unicorn_count * 5 + zebhor_count * 0.5
print("Win / Loss Calculations")
print("Unicorns:{}".format(unicorn_count))
print("zebras and horses:{}".format(zebhor_count))
print("Donkeys:{}".format(donkey_count))
print()
print("You spent:{}".format(HOW_MUCH))
print("Winnings:{:.2f}".format(winnings))