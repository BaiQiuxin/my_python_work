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
    """根据用户输入的名字，在字典文件中寻找其易位短语，输出最终找到的易位短语。"""
    name_letter_map = Counter(name)
    anagrams = []
    for word  in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"Numbers of remaining letters = {len(name)}")
    print(f"Numbers of remaining (real word) anagrams = {len(anagrams)}")

def process_choice(name):
    """检查输入用户的有效性，返回用户所做的选择及输入名字中剩余的字母"""
    while True:
        choice = input("\nMake a choice else Enter to start\
                       over or # to end: ")
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name)-len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = ''.join(left_over_list)
    return choice, name

def main():
    """根据用户输入的名字，生成易位短语"""
    name = ''.join(ini_name.lower().split())
    name = name.replace('_', '')
    limit = len(name)
    phrase = ''
    running = True
    
    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrase =", end=' ')
            print(phrase, file=sys.stderr)
            
            choice, name = process_choice(name)
            phrase += choice + ' '
        
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")
            print("Anagram of the name =", end=' ')
            print(phrase, file=sys.stderr)
            print()
            try_again