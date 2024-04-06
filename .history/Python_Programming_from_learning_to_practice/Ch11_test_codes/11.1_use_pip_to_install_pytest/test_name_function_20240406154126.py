# 向哲煜 2024.4.6

from name_function import get_formatted_name

def test_first_last_name():
    """能够正确的处理像Janis Joplin这样的名字吗"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name()