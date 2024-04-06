# 向哲煜 2024.4.3

from pathlib import Path

try:
    path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.3_abnormality/10.3_tests/cats.txt')
    contents = path.read_text()
    for content in contents:
        print(content)
    path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.3_abnormality/10.3_tests/')
except