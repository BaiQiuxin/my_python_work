# 向哲煜 2024.4.3

from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is Your name ? ")
    age = input("What is your age? ")
    location = input("Where do you live? ")
    contents = {
        'username': username,
        'age': age,
        'location': location,
    }
    contents = json.dumps(contents)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，并指出其姓名"""
    path = Path('Python_Programming_from_learning_to_practice/Ch10_files_and_abnormality/10.4_store_data/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back ,{username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()