def fibonacci(n):
     # Initialize the sequence with the first two Fibonacci numbers
  
  
    seq = [0, 1] 

    while len(seq) < n:
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)

    return seq

# Test the function with the given input
inpnumber = 5
answer = fibonacci(inpnumber)
print(answer)
