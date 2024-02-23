# 向哲煜 2024.2.23

#在给形参制定默认值时，等号两边不要有空格
def function_name(parameter_0, parameter_1='default value')
#函数调用中的关键字也应遵循这种约定
function_name(value_0, parameter_1='value')

#如果形参很多
def function_name_another(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body ...

#如果包含两个及以上函数，可使用两个空行来将相邻的函数分开

#所有import语句