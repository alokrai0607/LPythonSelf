def arrange_lowercase_first(input_str):
    lowerch = []
    upperch = []

    for char in input_str:
        if char.islower():
            lowerch.append(char)
        else:
            upperch.append(char)

    arrangedstr = ''.join(lowerch + upperch)
    return arrangedstr

string = "PyNaTive"
output = arrange_lowercase_first(string)
print(output)
