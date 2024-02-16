print("Welcome to the treasure island")
print("Your mission is to find the treasure")
print("You are at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input()
if direction == "left":
    print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across")
    lake = input()
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        color = input()
        if color == "yellow":
            print("You found the treasure! You win!")
        elif color == "red":
            print("It's a room full of fire. Game over")
        elif color == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You chose a door that doesn't exist. Game over")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game over")
    