# 向哲煜 2024.1.16

pizzas = ['PizzaPizza', 'CoachGreg', 'KFC']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really like pizza!")

friend_pizzas = pizzas[:]
pizzas.append('McDonald')
friend_pizzas.append('falafel')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)