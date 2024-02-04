# 向哲煜 2024.2.4

from curses import tigetflag
from turtle import title


polls = {
    'mike': [
        {
            'number': [1, 2, 3],
            'place': 'beijing',
            'pet': 'mouse',
        },
        
        {
            'username': 'mike10086',
            'ID': '020301',
        }
    ],
    
    'john': [
        {
            'number': [4, 5, 6],
            'place': 'paris',
            'pet': 'dormouse',
        },
        
        {
            'username': 'jack101',
            "ID": '258310'
        }
    ],
    
}

for name,infos in polls.items():
    print(f"\n{name.title()}")
    for info in infos:
        for key,value in info.items():
            print(f"{key.title()}: {value>title()}")