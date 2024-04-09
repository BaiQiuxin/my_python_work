"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

def recursive_finding_par():
    """递归寻找回文词"""
    

word_list = load_dictionary.load_file('2of4brif.txt')

pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))

# print in list format with no quotes or commas:
print(*pali_list, sep='\n')
