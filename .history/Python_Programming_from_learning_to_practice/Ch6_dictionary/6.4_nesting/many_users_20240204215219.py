users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")