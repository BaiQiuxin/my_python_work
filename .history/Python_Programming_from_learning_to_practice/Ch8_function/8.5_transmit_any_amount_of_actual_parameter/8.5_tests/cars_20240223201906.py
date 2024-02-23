# 向哲煜 2024.2.23

def make_car(manufacturer, model, **kwargs):
    """将一辆汽车的信息储存在字典中"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('subaru', 'outback', color)