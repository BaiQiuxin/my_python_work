# 向哲煜 2024.2.4

cities = {
    'new york': {
        'country': 'usa',
        'population': '3m',
        'fact': 'once belong to another country'
    },
    
    'beijing': {
        'country': 'china',
        'population': '20m',
        'fact': 'one of the oldest city'
    },
    
    'paris': {
        'country': 'france',
        'population': '1m',
        'fact': 'once belong to German'
    },
    
}

for city,infos in cities.items():
    print(f"Here are some information about {city.title()}:")
    for key,value in infos:
        print(f"{key.title()}")