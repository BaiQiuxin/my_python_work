# 向哲煜 2024.3.31

from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

#导入整个模块

import car
import electric_car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = electric_car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

#使用别名

from electric_car import ElectricCar as EC
