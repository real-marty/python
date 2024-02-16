print("Welcome to the tip calculator")
print("What was the total bill? ")
total_bill = float(input())
print("What percentage would you like to give? 10,12 or 15?")
percentage = int(input())
print("How many perople to split the bill?")
split = int(input())
each_pay = (total_bill * (1.0 + percentage / 100)) / split
print(f"Each person should pay: ${each_pay:.2f}")