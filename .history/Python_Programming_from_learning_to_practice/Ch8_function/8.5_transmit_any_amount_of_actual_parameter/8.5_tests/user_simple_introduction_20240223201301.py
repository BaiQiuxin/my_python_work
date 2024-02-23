# 向哲煜 2024.2.23

#使用任意数量的关键词实参
def build_profile(first, last, **user_info):            #两个星号**表示创建一个字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton',
                             field='physics')
print(user_profile)

my_introduction = build_profile('donald','trump',
                                )