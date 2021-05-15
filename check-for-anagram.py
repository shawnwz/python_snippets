#An anagram is a word that is formed by rearranging the letters of a different word, using all the original letters exactly once.
def check_anagram(first_word, second_word):
    return sorted(first_word) == sorted(second_word)

print(check_anagram("test", "tset"))
print(check_anagram("ginger", "danger"))