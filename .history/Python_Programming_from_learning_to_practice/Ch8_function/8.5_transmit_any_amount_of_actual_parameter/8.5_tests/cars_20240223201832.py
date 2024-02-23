# 向哲煜 2024.2.23

def store_cars(manufacturer, model, **kwargs):
    """将一辆汽车的信息储存在字典中"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return