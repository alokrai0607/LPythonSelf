def selection_sort(arr):
  
    num = len(arr)

    for i in range(num):

        min_index = i

        for j in range(i + 1, num):
         
            if arr[j] < arr[min_index]:
         
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr

input_list = [64, 25, 12, 22, 11]

sorted_list = selection_sort(input_list)

print(sorted_list)
