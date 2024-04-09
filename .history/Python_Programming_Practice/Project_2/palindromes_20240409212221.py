"""在字典文件中寻找回文单词"""

import load_dictionary

word_list = load_dictionary.load_file('./2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of palindromes found = {len(pali_list)}\n")
print(*pali_list, sep='\n')