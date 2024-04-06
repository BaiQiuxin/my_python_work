# 向哲煜 2024.3.31

from pathlib import Path

path = Path('pi')
contents = path.read_text()
print(contents)