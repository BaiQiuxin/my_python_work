# 向哲煜 2024.2.10

def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息

    Args:
        first_name (str): 名
        last_name (str): 姓
    """
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
        
    return person

musician = build_person('jimi', 'hendrix')
print(musician)