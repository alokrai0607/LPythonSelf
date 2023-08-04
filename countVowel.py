def count_vowels(input_string):
    vowels = "aeiouAEIOU"  
    vowel_count = 0       

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


mystr = "Hello"

res = count_vowels(mystr)

print("Number of vowels in the string:", res)
