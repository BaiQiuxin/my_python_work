# 向哲煜 2024.4.6

import pytest
from employee import Employee

@pytest.fixture
def  employee():
    """创建一个通用的测试实例"""
    

def test_give_default_raise():
    """测试年薪增长默认值是否可以正常运行"""
    employee = Employee('Albert', 'Einstein', 30_000)
    employee.give_raise()
    assert employee.yearly_salary == 35_000

def test_give_custom_raise():
    """测试年薪增长特定值是否可以正常运行"""
    employee = Employee('Albert', 'Einstein', 30_000)
    employee.give_raise(10_000)
    assert employee.yearly_salary == 40_000