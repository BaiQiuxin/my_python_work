# 向哲煜 2024.2.10

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回标准形式的姓名

    Args:
        first_name (str): 名
        last_name (str): 姓
    """
    full_name = f"{first_name} {}{last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)