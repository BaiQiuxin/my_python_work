# 向哲煜 2024.4.3

from pathlib import Path
import json

def get_stored_username(path):
    """如果"""


def greet_user():
    """问候用户，并指出其姓名"""
    path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.4_store_data/username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back ,{username}!")
    else:
        user_name = input("What is Your name ? ")
        contents = json.dumps(user_name)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {user_name}!")

greet_user()