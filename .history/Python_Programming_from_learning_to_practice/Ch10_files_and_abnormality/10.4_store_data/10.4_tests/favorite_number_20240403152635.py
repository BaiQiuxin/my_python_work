# 向哲煜 2024.4.3

from pathlib import Path
import json

path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.4_store_data/10.4_tests')

if path.exists():
    content = 
else:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("I remember what your favorite number is!")