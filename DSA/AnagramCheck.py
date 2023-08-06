def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


word1 = "cinema"
word2 = "iceman"

output = is_anagram(word1, word2)
print(output)
