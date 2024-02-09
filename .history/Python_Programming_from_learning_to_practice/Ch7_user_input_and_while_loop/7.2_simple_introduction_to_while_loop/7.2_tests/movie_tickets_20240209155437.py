# 向哲煜 2024.2.9

prompt = "\nPlease tell me how old you are, and I'll show you the price."
prompt += "\n(Enter 'quit' to end your input.)  "

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("The price is 0.")
        elif age >= 3 and age < 12:
            print("The price is $10.")
