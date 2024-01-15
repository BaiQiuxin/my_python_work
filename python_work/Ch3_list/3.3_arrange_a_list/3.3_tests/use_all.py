#向哲煜 2023.12.27
#创建一个列表，对于本章介绍的每个函数，都至少使用一次

#创建列表
anything_i_like = ['huangshan', 'changjiang', 'china', 'hefei', 'english', 'bodybuilding']
#打印列表
print(anything_i_like)
#打印列表元素
print(anything_i_like[0])
#调用列表元素
print(anything_i_like[0].title())
#负元素数的意义
print(anything_i_like[-1])
#使用列表元素
message = f"I like {anything_i_like[-1].title()} very much."
print(message)
#修改列表元素
print(anything_i_like)
anything_i_like[0] = 'huashan'
print(anything_i_like)
#末尾添加列表元素
anything_i_like.append('bicycle')
print(anything_i_like)
#插入列表元素
anything_i_like.insert(1,'painting')
print(anything_i_like)
#del删除列表元素（不可再访问）
del anything_i_like[1]
print(anything_i_like)
#pop()删除列表元素（可以接着使用它的值），相当于弹栈
popped = anything_i_like.pop(3)
print(popped)
print(anything_i_like)
#remove()根据值删除元素
river = 'changjiang'
anything_i_like.remove(river)
print(anything_i_like)
#sorted()临时排序
print(sorted(anything_i_like))
print(sorted(anything_i_like,reverse=True))
#reverse()倒着打印
anything_i_like.reverse()
print(anything_i_like)
anything_i_like.reverse()
print(anything_i_like)
#sort()永久排序
anything_i_like.sort()
print(anything_i_like)
anything_i_like.sort(reverse=True)
print(anything_i_like)
#len()确定列表长度
length_of_list = len(anything_i_like)
print(length_of_list)
