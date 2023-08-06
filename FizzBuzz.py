# def Fizzbuzz(n):
#     box = []

#     for num in range(1, n + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             box.append("FizzBuzz")
#             elif num % 3 == 0:
#                 box.append("Fizz")
#                 elif num % 5==0:
#                     box.append("Buzz")
#                     else:
#                         box.append(str(num))
#                         return ", ".join(box)


#                         Output = Fizzbuzz(10)
#                         print(output)

def fizzbuzz(n):
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return ", ".join(result)


output = fizzbuzz(100)
print(output)
