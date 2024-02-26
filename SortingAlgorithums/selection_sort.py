
# Find the minimum element in the unsorted part of the list and swap it with the first element in the unsorted part.
# Repeat this process until the list is sorted.




def selection_sort(arr):
 
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
    return arr
