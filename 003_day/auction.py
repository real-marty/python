import os
bidders = {}   
while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
    if more_bidders == "no":
        for key in bidders:
            if bidders[key] == max(bidders.values()):
                print(f"The winner is {key} with a bid of ${bidders[key]}")
        break
    else:
        continue
    



