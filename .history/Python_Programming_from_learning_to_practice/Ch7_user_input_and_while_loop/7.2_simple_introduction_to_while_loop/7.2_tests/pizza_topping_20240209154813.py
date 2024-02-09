# 向哲煜 2024.2.9

prompt = "\nPlease enter the kind of topping you want in your pizza:"
prompt += "\n(Enter 'quit' to end your input) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        p