def permutations(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        sub_permutations = permutations(remaining_chars)
        for perm in sub_permutations:
            result.append(first_char + perm)

    return result

# Input
input_string = "abc"

# Output
output = permutations(input_string)
print(output)
