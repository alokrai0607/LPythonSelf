# Function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function with the given input
number = 5
answer = factorial(number)
print(f"Factorial of {number} is {answer}.")


# Function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test the function with the given input
print(factorial(5))  # 120
