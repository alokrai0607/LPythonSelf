def is_palindrome(string):
    string = string.lower().replace(" ", "")  
    return string == string[::-1]

inputStr = "madam"

if is_palindrome(inputStr):
    print(f"The word {inputStr} is a palindrome.")
else:
    print(f"The word {inputStr} is not a palindrome.")
