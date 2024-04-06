# 向哲煜 2024.4.6

def get_formatted_name(first, last, middle=''):
    """生成格式规范的姓名"""
    if middle:
        full_name = f"{first} {middle}"
    full_name = f"{first} {last}"
    return full_name.title()