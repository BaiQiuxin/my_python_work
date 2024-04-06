# 向哲煜 2024.4.1

from pathlib import Path

user_name = input("Please enter your name: ")

path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.2_write_files/10.2_tests/guest.txt')
path.write_text()