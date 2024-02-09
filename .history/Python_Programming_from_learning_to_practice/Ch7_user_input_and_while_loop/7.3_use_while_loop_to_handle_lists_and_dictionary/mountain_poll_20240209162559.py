# 向哲煜 2024.2.9

responses = {}
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #将回答存储在字典中
    responses[name] = response
    
    #看看是否还有人要参与调查
    repeat = input()