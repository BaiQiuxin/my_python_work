# 向哲煜 2024.1.16

# 切片（slice）

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])          #如果没有指定起始索引将自动从列表开头开始
print(players[2:])          #同样的，如果没有指定终止索引将自动在列表末尾结束
print(players[-3:])         #负号索引返回与列表末尾有相应距离的元素，这样也可以输出最后三位队员的名字

#遍历切片

print("Here are the first three players on my teams:")
for player in players[:3]:
    print(player.title())
