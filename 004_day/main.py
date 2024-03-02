def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

operations = {
    "*": multiply,
    "+": add,
    "-": subtract,
    "/": divide
}

def calc(prev_result):
    print("Enter an operation: ")
    operation = input()
    if operation in operations:
        print("Enter a second number: ")
        num = float(input())
        result = operations[operation](prev_result, num)
        print(f"Result: {result}")
        return result
    else:
        print("Invalid operation")
        return prev_result
        
        
print("Welcome to the calculator")
print("Enter a first number: ")
number = float(input())   
while True:
    number = calc(number)
    print("Do you want to continue? (y/n)")
    cont = input()
    if cont == "n":
        break
    elif cont == "y":
        print("Your first number is: " + str(number))
    else:
        print("Invalid input")
        break