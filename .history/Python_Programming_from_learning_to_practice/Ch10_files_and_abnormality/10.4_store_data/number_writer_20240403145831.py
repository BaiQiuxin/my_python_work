# 向哲煜 2024.4.2

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.4_store_data')
contents = json.dumps(numbers)
path.write_text(contents)