# 向哲煜 2024.3.31

from pathlib import Path

path = Path('pi_digits')
contents = path.read_text()
print(contents)