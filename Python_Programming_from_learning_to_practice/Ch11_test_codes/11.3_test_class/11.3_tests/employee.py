# 向哲煜 2024.4.6

class Employee:
    """一个模拟雇员的尝试"""
    
    def __init__(self, first_name, last_name, yearly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = yearly_salary
    
    def give_raise(self, increment = 5000):
        """年薪默认增加5000美元"""
        self.yearly_salary += increment