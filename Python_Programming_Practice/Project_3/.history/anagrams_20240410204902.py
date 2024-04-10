""""""

import load_dictionary

word_list = load_dictionary.load_file('/Project_3/2of4brif.txt')

anagram_list = []

# 输入一个单词或名字，下面代码的功能是找到这些单词或者名字对应的所有易位词
name = 'Foster'
print(f"Input name = {name}")
name = name.lower()
print(f"Using name = {name}")

# 按照字母表顺序对变量name中的字符串排序，并寻找其易位词
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# 输出易位词列表
print("\n")
if len(anagram_list) == 0:
    print("You need a large ")