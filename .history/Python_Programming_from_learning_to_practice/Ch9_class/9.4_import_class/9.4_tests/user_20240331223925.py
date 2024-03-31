# 向哲煜 2024.3.31
"""一组模拟用户的类"""
class User:
    """介绍用户"""
    
    def __init__(self, first_name, last_name, age, location, job):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.job = job
        self.login_attempts = 0
    
    def describe_user(self):
        """打印用户信息摘要"""
        print(f"\nThe name of the user is {self.first_name.title()} {self.last_name.title()}.")
        print(f"The age of the user is {self.age}.")
        print(f"The location of the user is {self.location.title()}")
        print(f"The job of the user is {self.job}.")
    
    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}.")
        print("Welcome to our community!")
    
    def increment_login_attempts(self):
        """将登入尝试加一"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """将登入尝试次数重置为0"""
        self.login_attempts = 0
        
        