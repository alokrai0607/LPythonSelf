# Method 1: Using a for loop
  
# Initialize an empty list

List = []
for i in range(1, 11):
    List.append(i)

print(List)   # [1,2,3,4,5,6,7,8,9,10]

List.append(15)
List.append(16)
List.append(17)
List.append(18)
List.append(19)

print(List)   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19]

List.remove(1)
List.remove(3)
List.remove(5)
List.remove(7)
List.remove(10)

print(List)  # [2, 4, 6, 8, 9, 15, 16, 17, 18, 19]  

List.append(1)
List.append(2)
List.append(3)
List.append(4)
List.append(5)

print(List)  # [2, 4, 6, 8, 9, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5]

List.sort()

print(List)  # [1, 2, 2, 3, 4, 4, 5, 6, 8, 9, 15, 16, 17, 18, 19]

List.sort(reverse=True)

print(List)