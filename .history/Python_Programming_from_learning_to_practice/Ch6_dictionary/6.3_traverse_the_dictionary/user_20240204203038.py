# 向哲煜 2024.2.4

#遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key,value in user_0.items():
    print(f"\nKey : {key}")
    print(f"Value : {value}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name,language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#遍历字典中的所有键
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_language.keys():
    print(name.title())

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['sarah', 'phil']
for name in favorite_language.keys():
    print(f"Hi, {name.title()}")
    
    if name in friends:
        