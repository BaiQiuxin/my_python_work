# 向哲煜 2024.2.9

#让用户选择何时退出
prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)