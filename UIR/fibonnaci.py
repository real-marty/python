#todo make bibbonaci sequencu using recursion and non-recursion method

def fib(n):
    if n < 0:
        print("fib - starts with 0")
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_non_recursion(n):
    if n < 0:
        return "fib - starts with 0"
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a

print(fib(10))
print(fib_non_recursion(10))
