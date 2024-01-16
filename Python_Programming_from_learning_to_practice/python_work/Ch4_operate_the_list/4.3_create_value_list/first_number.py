# 向哲煜 2024.1.16

#使用range()函数

for value in range(1, 5):
    print(value)                #并不打印5

for value in range(6):
    print(value)                #只指定一个参数将从0开始

#使用range()创建数值列表

numbers = list(range(1,6))
print(numbers)

#range()函数还可以指定步长

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)       #还可以用squares.append(value ** 2)使代码更简洁

print(squares)