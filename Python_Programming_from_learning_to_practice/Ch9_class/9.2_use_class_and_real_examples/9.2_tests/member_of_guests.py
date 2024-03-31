# 向哲煜 2024.3.13

class Restaurant:
    """一个模拟餐馆的简单尝试"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """打印前述两项信息"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")
    
    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number
    
    def increment_number_served(self, increment):
        """使就餐人数递增"""
        self.number_served += increment

restaurant = Restaurant('Ciao', 'Italian')
print(f"The name of the restaurant is {restaurant.restaurant_name}.")
print(f"The type of it's cuisine is {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)

restaurant.set_number_served(100)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)