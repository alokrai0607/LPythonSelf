

# Choose a pivot element and partition the list into elements less than the pivot and elements greater than the pivot.
# Recursively sort the two partitions.



def quick_sort(arr):
   
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
   
    left = [x for x in arr if x < pivot]
   
    middle = [x for x in arr if x == pivot]
   
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


