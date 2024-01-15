#向哲煜 2023.12.27

#sort()对列表永久排序
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort()                                     #正向排序
print(cars)

cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort(reverse=True)                         #反向排序
print(cars)

#sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyato', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))                             #正向排序
print(sorted(cars,reverse=True))                #反向排序

print("\nHere is the original list again:")
print(cars)

#reverse()倒着打印列表
cars = ['bmw', 'audi', 'toyato', 'subaru']
print(cars)

cars.reverse()                                  #虽然是永久性反转，但可以随时通过再次调用reverse恢复到原来的排列顺序
print(cars)

#len()确定列表的长度
cars = ['bmw', 'audi', 'toyato', 'subaru']
print(len(cars))