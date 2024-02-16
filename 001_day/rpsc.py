rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
print("Welcome to Rock Paper Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

rpc = [rock, paper, scissors]

lose = "You lose"
win = "You win"

print(f"You chose: {rpc[user_choice]}")
print(f"Computer chose: {rpc[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
    print(lose)
else:
    print(win)
        
    