#向哲煜 2023.12.24

#修改列表元素
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

#添加列表元素
#末尾添加
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)
#可以先创建一个空列表，再动态的在末尾添加元素
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)
#在列表中插入元素
motocycles = ['honda', 'yamada', 'suzuki']
motocycles.insert(0, 'ducati')
print(motocycles)

#删除列表元素
#del删除（不可再访问）
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)

del motocycles[0]
print(motocycles)
#pop()删除 （可以接着使用它的值）
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)
#相当于弹栈
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

motocycles = ['honda', 'yamada', 'suzuki']
last_owned = motocycles.pop()
print(f"The last motocycle I owned was a {last_owned.title()}")
#实际上，pop()可以弹出列表任意位置的元素
motocycles = ['honda', 'yamada', 'suzuki']

first_owned = motocycles.pop(0)
print(f"The first motobicycle I owned was a {first_owned.title()}")
#remove()删除元素（根据值删除元素）
motocycles = ['honda', 'yamada', 'suzuki', 'ducati']
print(motocycles)

motocycles.remove('ducati')
print(motocycles)
#remove()删除也可以继续使用它的值
motocycles = ['honda', 'yamada', 'suzuki', 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive fpr me")
#remove()只会删除第一个指定的值，如果要删除的值出现多次，就需要使用循环来确保将每个值都删除