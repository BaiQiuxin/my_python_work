# 向哲煜 2024.2.23

#导入整个模块
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#导入特定的函数
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用as给函数制定别名
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用as给模块指定别名
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#导入模块中的所有函数
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#最好不要使用这种导入方法，因为模块中如果有函数的名称与当前项目中既有的名称相同，可能导
#致意想不到的结果：Python可能会因为遇到多个名称相同的函数或变量而覆盖函数，而不是分别导
#入所有的函数

#最佳的做法是，要么只导入需要使用的函数，要么导入整个模块