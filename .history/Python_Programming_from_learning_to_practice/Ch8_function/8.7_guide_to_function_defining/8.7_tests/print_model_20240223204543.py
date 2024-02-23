# 向哲煜 2024.2.23

#import module_name
import print_function
print_function.print_model('tiger')

#from module_name import function_name
from print_function import print_model
print_model('lion')

#from module_name import function_name as fn
from print_model import print_model as pm
pm('cat')

#import module_name as mn
import print_model as prm
prm.print_model('dog')

#from module_name import *
from print_model import *