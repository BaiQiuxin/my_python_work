# 向哲煜 2024.3.31

class Restaurant:
    """一个模拟餐馆的简单尝试"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """打印前述两项信息"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

class IceCreamStand(Restaurant):
    """"""