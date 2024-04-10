"""
"""

import sys
from collections import Counter

import load_dictionary

dict_file = load_dictionary.load_file('2of4brif.txt')
#保证下面使用的字母"a"和"I"都是小写。
dict_file.append('a')