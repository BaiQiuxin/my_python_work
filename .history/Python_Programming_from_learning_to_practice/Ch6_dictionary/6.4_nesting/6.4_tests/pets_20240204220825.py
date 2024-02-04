# 向哲煜 2024.2.4

ari = {
    'type': 'fox',
    'master': 'mike',
}

tom = {
    'type': 'cat',
    'master': 'jack',
}

jerry = {
    'type': 'dormouse',
    'master': 'john',
}

pets = [ari, tom, jerry]

for pet in pets:
    print(f"{pet}")
    for key,value in pet.items():
        print(f"{key.title()}: {value.title()}")