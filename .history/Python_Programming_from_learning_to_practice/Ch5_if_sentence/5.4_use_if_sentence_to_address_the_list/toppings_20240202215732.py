# 向哲煜 2024.2.2

#检查特殊元素
from turtle import pen


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

#确定列表非空
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms' ,'olives', 'green peppers', 'pepperoni', 
                    'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {}")