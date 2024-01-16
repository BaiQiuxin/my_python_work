# 向哲煜 2024.1.16

#定义元组

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#不可以这样做
#dimensions[0] = 250

#严格地说，元组是由逗号标识的，圆括号只是让元组看起来更加整洁、更清晰。如果你想要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
#   my_t =(3,)
#创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。

#遍历元组中的所有值

for dimension in dimensions:
    print(dimension)

#修改元组变量

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)