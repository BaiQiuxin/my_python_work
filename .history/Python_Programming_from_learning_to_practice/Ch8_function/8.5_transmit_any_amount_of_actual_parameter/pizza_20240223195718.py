# 向哲煜 2024.2.23

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_another(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza_another('pepperoni')
make_pizza_another('mushrooms', 'green peppers', 'extra cheese')

#结合使用位置实参和任意数量的实参
def make_pizza_one(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza ")