# 向哲煜 2024.2.10

def get_formatted_name (first_name, last_name):
    """返回规范形式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f)