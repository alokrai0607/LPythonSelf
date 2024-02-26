

# Iterate over the list, and for each element, move it to its correct position in the sorted part of the list.
# The sorted part starts with the first element and grows by one element on each iteration.



def insertion_sort(arr):

    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
       
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
