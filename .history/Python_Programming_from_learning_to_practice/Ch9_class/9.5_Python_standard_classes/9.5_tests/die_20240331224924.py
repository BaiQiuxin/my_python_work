# 向哲煜 2024.3.31
"""一个模拟色子的类"""

from random import ran

class Die:
    """一次模拟色子的尝试"""
    
    def __init__(self, sides=6):
        """初始化色子面数"""
        self.sides = sides
    
    def roll_die(self):
        """模拟一次掷色子的结果"""
        