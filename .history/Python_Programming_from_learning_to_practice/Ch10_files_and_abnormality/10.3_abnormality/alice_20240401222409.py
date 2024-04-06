# 向哲煜 2024.4.1

from pathlib import Path

path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.3_abnormality/alice.txt')
try:
    contents = path.read_text(encoding= 'utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does ont exist.")
else:
    #计算文件大概包含多少个单词
    words = contents.split()
    num_words = words