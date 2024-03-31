# 向哲煜 2024.3.31
"""一组用于模拟管理员及其权限的类"""
from user import User

class Privileges:
    """管理员的权限"""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """初始化权限"""
        self.privileges = privileges
    
    def show_privileges(self):
        """打印管理员的权限"""
        print(self.privileges)



class Admin(User):
    """介绍管理员"""
    
    def __init__(self, first_name, last_name, age, location, job):
        """初始化属性"""
        super().__init__(first_name, last_name, age, location, job)
        self.privileges = Privileges()