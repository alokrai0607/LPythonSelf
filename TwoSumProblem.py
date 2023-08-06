def two_sum(nums, target):
    numDict = {} 

    for i, num in enumerate(nums):
        complement = target - num
        if complement in numDict:
            return [numDict[complement], i]
        numDict[num] = i  

    return None 
    
nums = [2, 7, 11, 15]
target = 9

output = two_sum(nums, target)
print(output)
