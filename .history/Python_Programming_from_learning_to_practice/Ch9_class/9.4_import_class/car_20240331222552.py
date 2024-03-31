# 向哲煜 2024.3.31
"""一组用于表示燃油汽车和电动汽车的类"""

class Car:
    """一次模拟汽车的尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """打印一条消息，指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """让里程表读数增加指定的值"""
        self.odometer_reading += miles



class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电池续航里程的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car)