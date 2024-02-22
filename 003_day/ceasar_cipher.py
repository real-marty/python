import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ask_user_for_values():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return direction, text, shift


def ceasar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += letter
    print(f"The {direction}d text is {result}")


print(art.logo)
direction, text, shift = ask_user_for_values()
ceasar(text, shift, direction)

while True:
    print("Would you like to go again?")
    user_input = input("Type 'yes' to go again or 'no' to stop: ")
    if user_input != "yes":
        break
    elif user_input == "yes":
        direction, text, shift = ask_user_for_values()
    ceasar(text, shift, direction)
    
    
    


