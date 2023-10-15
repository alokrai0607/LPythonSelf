# squares = [i ** 2 for i in range(1, 11)]
# print(squares)


def square_numbers(input_list):

    squared_numbers = [num**2 for num in input_list]

    return squared_numbers


inputNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

answer = square_numbers(inputNum)

print(answer)  
