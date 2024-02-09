# 向哲煜 2024.2.9

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you have finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#在所有python循环中都可以使用break语句。例如