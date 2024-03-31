# 向哲煜 2024.3.31

class User:
    """介绍用户"""
    
    def __init__(self, first_name, last_name, age, location, job):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.job = job
    
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



class Privileges:
    """管理员的权限"""
    def __init__(self, privileges):
        self.privileges = privileges



class Admin(User):
    """介绍管理员"""
    
    def __init__(self, first_name, last_name, age, location, job, privileges=['can add post', 'can delete post', 'can ban user']):
        super().__init__(first_name, last_name, age, location, job)
        self.privileges = privileges
    
    def show_privileges(self):
        """打印管理员的权限"""
        print(self.privileges)
