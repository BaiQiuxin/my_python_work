# 向哲煜 2024.4.6

from employee import Employee

def test_give_default_raise():
    """测试年薪增长默认值是否可以正常运行"""
    employee = Employee('Albert', 'Einstein', 30_000)
    employee.give_raise()
    assert employee.yearly_salary == 35_000

def test_give_custom_raise():
    """测试年薪增长特定值是否可以正常运行"""
    employee = Employee('Albert', 'Einstein', 30_000)
    employee.give_raise(10)