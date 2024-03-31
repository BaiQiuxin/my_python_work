#向哲煜 2024.3.3
class Dog:                  #根据约定，在Python中首字母大写指的是类
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name ,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

#根据类创建实例
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()