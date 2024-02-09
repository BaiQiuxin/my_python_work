# 向哲煜 2024.2.9

prompt = "\nPlease enter the kind of topping you want in your pizza:"
prompt += "\n(Enter 'quit' to end your input) "

while :
    topping = input(prompt)
    print(f"\nPlease adding {topping} to the pizza.")

active = True
while active:
    topping = input(prompt)
    
    if topping == 'quit':
        active = False
    else:
        print(f"\nPlease adding {topping} to the pizza.")

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"\nPlease adding {topping} to the pizza.")