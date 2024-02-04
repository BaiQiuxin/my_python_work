# 向哲煜 2024.2.4

#由类似的对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}")

#使用get()来访问值
alien_0 = {
    'color': 'green',
    'speed': 'slow',
}
point_value = alien_0.get()
print(alien_0['points'])