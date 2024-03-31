#向哲煜 2024.3.3

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

user_one = User('Mike', 'meadows', 18, 'new york', 'doctor')
user_one.describe_user()
user_one.greet_user()

user_two = User('John', 'wick', 24, 'london', 'actor')
user_two.describe_user()
user_two.greet_user()

user_three = User('tom', 'jerry', 30, 'washington', 'animal')
user_three.describe_user()
user_three.greet_user()