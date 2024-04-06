# 向哲煜 2024.4.1

from pathlib import Path

path = Path('E:/VSCode/python/Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.1_read_files/10.1_tests/learning_python.txt')

note = path.read_text()

note = note.rstrip()

print(note)

lines = path.read_text()