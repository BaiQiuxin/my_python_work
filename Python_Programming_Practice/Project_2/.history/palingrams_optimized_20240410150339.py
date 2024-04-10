"""在字典文件中寻找回文单词"""

import time

import load_dictionary

word_list = load_dictionary.load_file('2of4brif.txt')

# 寻找回文短语
def find_palingrams():
    """寻找字典中的回文短语。"""
    pali_list = []
    words = set(word_list)
    for word in words:
             end = len(word)
             rev_word = word[::-1]
             if end > 1:
                 for i in range(end):
                  ➌ if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                        pali_list.append((word, rev_word[end-i:]))
                  ➍ if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                        pali_list.append((rev_word[:end-i], word))
        return pali_list
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/epubit17/article/details/120109525

start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
# 根据短语的第一个单词，对回文短语进行排序
palingrams_sorted = sorted(palingrams)

print(f"\nNumber of palindromes found = {len(palingrams_sorted)}\n")
for first, second in palingrams_sorted:
    print(f"{first} {second}")

print(f"Runtime for this program was {end_time-start_time} seconds.")
