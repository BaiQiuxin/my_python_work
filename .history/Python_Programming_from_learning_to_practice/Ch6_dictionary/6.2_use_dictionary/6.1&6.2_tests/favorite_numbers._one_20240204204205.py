# 向哲煜 2024.2.4

favorite_numbers = {
    'mike': 0,
    'jack': -1,
    'rose': 3.1415926,
    'eric': 1,
    'peter': 5,
}

names = ['mike', 'jack', 'rose', 'eric', 'peter']
for name in names:
    print(f"{name.title()}'s favorite number is {favorite_numbers[name]}")