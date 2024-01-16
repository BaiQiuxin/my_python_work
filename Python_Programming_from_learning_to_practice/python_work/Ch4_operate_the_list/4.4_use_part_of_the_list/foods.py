# 向哲煜 2024.1.16

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]          #创建副本

my_foods.append('cannoli')
friend_foods.append('ice cream')

#这样是行不通的:
#friend_foods = my_foods 这样两个变量实际上就指向了同一个列表

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
