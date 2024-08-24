#List
Favorite_fruits = ["Banana" , "Apple" , "Guava" , "Pineapple" , "Mango"]
Favorite_fruits.append("Orange") #It will add in list
print(Favorite_fruits)


#tuple
Favfruits = ("Banana" , "Apple" , "Guava" , "Pineapple" , "Mango")
#it will not add because tuple is immutable Datatype.
print(Favfruits)


my_tuple = (1, 2, 3)
new_element = 4

# Convert the tuple to a list
my_list = list(my_tuple)

# Add the new element to the list
my_list.append(new_element)

# Convert the list back to a tuple
new_tuple = tuple(my_list)

print(new_tuple)