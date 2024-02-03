str = "i am studying Python from apna college college"

# endswith
print(str.endswith("llege"))  #True
print(str.endswith("lle"))   #False

#startswith
print(str.startswith("A")) #False
print(str.startswith("i")) #True

#Capitalize
print(str.capitalize()) #I am studying python from apna college
print(str)     # i am studying Python from apna college

#replace (Python will replace with java)
print(str.replace("Python","Java"))


#find(it will search which find first in sentence or world and it will return their index)
print(str.find("a"))  #2
print(str.find("from"))  #21 (it will return index of only "f" not for "from" )
print(str.find("z"))  #result will be -1 because it will not find any charecter wich starts with "z"

#count
print(str.count("college"))  # Result will be  because college comes under string  times .