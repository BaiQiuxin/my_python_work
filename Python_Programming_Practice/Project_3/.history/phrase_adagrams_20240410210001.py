"""
"""

import sys
from collections import Counter

import load_dictionary

dict_file = load_dictionary.load_file('2of4brif.txt')
#保证下面使用的字母"a"和"I"都是小写。
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Please enter a name: ")

def find_anagrams(name, word_list):
    """根据用户输入的名字，在字典文件中寻找其易位短语"""