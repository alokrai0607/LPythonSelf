
    # **Maximum Subarray**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
    # - *Input*: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # - *Output*: "6"

# Input
inputArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubarraySum(nums):
    maxSum = nums[0]
    currSum = nums[0]

    for num in nums[1:]:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum



# Output
output = maxSubarraySum(inputArray)
print(output)
