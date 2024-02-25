def fibonacci(n):
     # Initialize the sequence with the first two Fibonacci numbers
  
  
    sequence = [0, 1] 

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Test the function with the given input
inpnumber = 5
answer = fibonacci(inpnumber)
print(answer)
