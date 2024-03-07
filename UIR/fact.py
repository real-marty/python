# todo make factorial using the recursion and non-recursion method

def fact(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)

def fact_non_recursion(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(fact(5));
print(fact_non_recursion(0));
