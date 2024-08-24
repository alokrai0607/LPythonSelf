list = [5,9,7,8,1,3,2]


#append(element)
list.append(0)
print(list)    #[5, 9, 7, 8, 1, 3, 2, 0]

#sort
list.sort()
print(list)  #[0, 1, 2, 3, 5, 7, 8, 9]

#sort + reverse Order
list.sort(reverse=True)
print(list)  #[9, 8, 7, 5, 3, 2, 1, 0]

#reverse
list.reverse()
print(list)  #[0, 1, 2, 3, 5, 7, 8, 9]

#insert(index,value)
list.insert(5,6)
print(list)   #[0, 1, 2, 3, 5, 6, 7, 8, 9]

str = ['z','d','s','a','c']
#sort
str.sort() #['a', 'c', 'd', 's', 'z']

#sort(reverse=True)
str.sort(reverse=True)
print(str)  #['z', 's', 'd', 'c', 'a']

#remove
str.remove("d")
print(str) #['z', 's', 'c', 'a']


#pop
str.pop(-2)
print(str) #['z', 's', 'a']