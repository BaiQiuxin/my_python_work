# 向哲煜 2024.4.6

from city_functions import get_formatted_city_location

def test_city_country():
    """测试Santiago， Chile能否通过测试"""
    location = get_formatted_city_location('santiago', 'chile')
    assert location == 'Santiago, Chile'

def test_city_country_population():
    """测试Santiago，Chile，population=500_000能否通过测试"""
    location = get_formatted_city_location('santiago', 'chile', 500_000)
    assert location