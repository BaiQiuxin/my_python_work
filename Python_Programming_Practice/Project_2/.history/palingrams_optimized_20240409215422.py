"""在字典文件中寻找回文单词"""

import load_dictionary

word_list = load_dictionary.load_file('2of4brif.txt')

# 寻找回文短语
def find_palingrams():
    """寻找字典中的回文短语"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                
    return pali_list

palingrams = find_palingrams()
# 根据短语的第一个单词，对回文短语进行排序
palingrams_sorted = sorted(palingrams)

print(f"\nNumber of palindromes found = {len(palingrams_sorted)}\n")
for first, second in palingrams_sorted:
    print(f"{first} {second}")
