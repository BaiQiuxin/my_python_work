# 向哲煜 2024.2.10

def city_country(city_name, country_name):
    """返回城市及其对应的国家"""
    pair = f"{city_name.title()}, {country_name.title()}"
    return pair

city_one = city_country('santiago', 'chile')
print(city_one)

city_two = city_country('beijing', 'china')
print(city_two)