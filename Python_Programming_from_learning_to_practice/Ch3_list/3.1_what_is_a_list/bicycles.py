#向哲煜 2023.12.23 

#列表是什么
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[3])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-2])

#使用列表中的各个值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"

print(message)