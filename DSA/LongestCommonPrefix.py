def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()
   
    first_str = strs[0]
    last_str = strs[-1]

    # Find the common prefix between the first and last strings
    common_prefix = []

    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break


    return "".join(common_prefix)

# Input
str_list = ["flower", "flow", "flight"]


# Output
output = longest_common_prefix(str_list)
print(output)
