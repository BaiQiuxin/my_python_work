# 向哲煜 2024.4.1

from pathlib import Path

from certifi import contents

user_counter = 1
contents = ''

while user_counter < 6:
    user_name = input("Please enter your name: ")
    contents += user_name