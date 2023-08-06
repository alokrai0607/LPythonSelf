def addnage(dictionary, name, age):
    dictionary[name] = age

def updage(dictionary, name, newage):
    if name in dictionary:
        dictionary[name] = newage

def delname(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Input
mydict = {}
addnage(mydict, "John", 25)
updage(mydict, "John", 26)
delname(mydict, "John")

# Output
print("{}".format(mydict))
