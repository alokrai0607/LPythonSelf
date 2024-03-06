def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) //2
    array_sum = sum(nums)
    missingNumber = total_sum - array_sum
    return missingNumber


input_array = [3, 0, 1, 2]

output = missingNumber(input_array)
print(output)
