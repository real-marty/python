import random


print("Welcome to password generator")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("How many letters would you like in your password?")

nr_letters = int(input())

print("How many symbols would you like in your password?")

nr_symbols = int(input())

print("How many numbers would you like in your password?")

nr_numbers = int(input())

password = []

for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
    
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
    
random.shuffle(password)

final_password = ""

for char in password:
    final_password += char
    
print(f"Your password is: {final_password}")
