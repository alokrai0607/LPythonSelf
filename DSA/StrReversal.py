def reverse_string_loop(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


original_string = "Python"
reversed_string = reverse_string_loop(original_string)
print(reversed_string)
