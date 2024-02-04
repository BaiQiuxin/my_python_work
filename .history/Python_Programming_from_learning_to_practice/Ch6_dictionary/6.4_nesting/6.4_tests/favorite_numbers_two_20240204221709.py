# 向哲煜 2024.2.4

favorite_numbers = {
    'mike': [0, 5, 10],
    'jack': [-1, 2.718281],
    'rose': [3.1415926, 1.414],
    'eric': [1, 0, -1],
    'peter': [3, 6, 9],
}

for person,numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are as follows:")
    for number in numbers:
        print(f"\t{number}")