# 向哲煜 2024..4.3

from pathlib import Path
import json

user_name = input("What is your name? ")

path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.4_store_data/username.json')
contents = json.dumps(user_name)