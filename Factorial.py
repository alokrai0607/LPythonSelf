
# Factorial Algorithm:

# Input the number n for which you want to calculate the factorial.
# Set a variable result to 1 (initial value for the factorial).
# Use a loop that starts from 1 and goes up to n.
# Multiply result with the loop variable in each iteration.
# Update the result variable with the new value.
# After the loop, the result variable will contain the factorial of n.


#Way-1

# # Function
# def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# # Test the function with the given input

number = 5
answer = factorial(number)
print(f"Factorial of {number} is {answer}.")

#####################################################################################

#Way-2

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))  #120

