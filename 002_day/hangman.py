

word_list = ["aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hippo", "kangaroo", "lion", "monkey", "newt", "otter", "panda", "quail", "rabbit", "sheep", "tiger", "unicorn", "vulture", "walrus", "xerus", "yak", "zebra"]


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

chosen_word = random.choice(word_list)
mistakes = 0
hidden_word = []
for letter in chosen_word:
    hidden_word.append("_")


print("Welcome to Hangman!")
print("Write a letter to guess the word")
print("You have 6 chances to guess the word\n")
WORD_MESSAGE = "Your word is: "
print(WORD_MESSAGE + " ".join(hidden_word))



while mistakes <= 7:
    letter = input("Write a letter: ").lower()
    if letter in chosen_word and letter not in hidden_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == letter:
                hidden_word[position] = letter
        print(WORD_MESSAGE + " ".join(hidden_word) + "\n")
        if "_" not in hidden_word:
            print("You win!")
            break
    else:
        mistakes += 1
        print("You have " + str(6 - mistakes) + " chances left")
        if mistakes == 7:
            print("You lose!")
            print(stages[-mistakes] + "\n")
            break
        print(WORD_MESSAGE + " ".join(hidden_word) + "\n")
        print(stages[-mistakes] + "\n")
            
        

