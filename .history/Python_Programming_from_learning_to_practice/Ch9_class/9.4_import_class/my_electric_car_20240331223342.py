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

from class Parrot:

 def fly(self):
   print('Parrot can fly')

 def swim(self):
   print('Parrot can not swim')

class Penguin:

 def fly(self):
   print('Penguin can not fly')

 def swim(self):
   print('Penguin can swim')

# common interface
def flying_test(bird):
  bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)