"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

def recursive_finding_palindromes(word_list):
    """递归寻找回文词"""
    pali_list = []
    word = word_list[0]
    if word:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)
        else:
            recursive_finding_palindromes(word_list.remove(word))
    else:
        return pali_list

word_list = load_dictionary.load_file('2of4brif.txt')

pali_list = recursive_finding_palindromes(word_list)

print(f"\nNumber of palindromes found = {len(pali_list)}\n")
# print in list format with no quotes or commas:
print(*pali_list, sep='\n')
