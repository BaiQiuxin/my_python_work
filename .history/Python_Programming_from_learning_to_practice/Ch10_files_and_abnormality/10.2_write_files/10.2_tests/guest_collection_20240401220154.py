# 向哲煜 2024.4.1

from pathlib import Path

user_counter = 1
contents = ''

while user_counter < 6:
    user_name = input("Please enter your name: ")
    contents += user_name

path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/')