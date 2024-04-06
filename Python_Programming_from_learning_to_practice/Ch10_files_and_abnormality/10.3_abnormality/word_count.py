# 向哲煜 2024.4.1

from pathlib import Path

def count_words(path):
    """计算一个文件大概含有多少个单词"""
    try:
        contents = path.read_text(encoding= 'utf-8')
    except FileNotFoundError:
        #print(f"Sorry, the file {path} does ont exist.")
        pass
    else:
        #计算文件大概包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.3_abnormality/alice.txt')
count_words(path)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
