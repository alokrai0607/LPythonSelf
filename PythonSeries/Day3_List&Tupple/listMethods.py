list = [5,9,7,8,1,3,2]
list.append(0)
print(list)    #[5, 9, 7, 8, 1, 3, 2, 0]

list.sort()
print(list)  #[0, 1, 2, 3, 5, 7, 8, 9]

list.sort(reverse=True)
print(list)  #[9, 8, 7, 5, 3, 2, 1, 0]

list.reverse()
print(list)  #[0, 1, 2, 3, 5, 7, 8, 9]

list.insert(5,6)
print(list)   #[0, 1, 2, 3, 5, 6, 7, 8, 9]