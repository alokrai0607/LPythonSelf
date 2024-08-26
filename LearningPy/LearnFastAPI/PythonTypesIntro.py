# Python has support for optional "type hints" (also called "type annotations").
# These "type hints" or annotations are a special syntax that allow declaring the type of a variable.
# FastAPI is all based on these type hints.


# Let's start with a simple example:
def get_fullName (firstName , lastName) :
    fullName = firstName.title()+" "+lastName.title()
    return fullName

#print(get_fullName("Alok" , "Rai"))

# Let's start with Add types :
def get_fullName (firstName:str , lastName:str) : #after adding data type in this line of code it is suggesting for title function automatically .
    fullName = firstName.title()+" "+lastName.title()
    return fullName

print(get_fullName("Alok" , "Rai"))


