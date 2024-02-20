# 向哲煜 2024.2.10

def greet_user(names)；
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)