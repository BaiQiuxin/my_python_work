# 向哲煜 2024.4.1

from pathlib import Path

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'

path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.2_write_files/programming.txt')
path.write_text('')