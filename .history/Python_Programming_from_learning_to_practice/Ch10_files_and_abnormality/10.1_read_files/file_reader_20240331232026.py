# 向哲煜 2024.3.31

from pathlib import Path

path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.1_read_files/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))