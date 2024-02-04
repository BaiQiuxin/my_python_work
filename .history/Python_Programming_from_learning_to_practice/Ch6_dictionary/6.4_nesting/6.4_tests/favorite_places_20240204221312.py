# 向哲煜 2024.2.4

favorite_places = {
    'jack': ['beijing', 'mountain tai', 'tibet'],
    'mike': ['new york'],
    'john': ['princeton', 'paris'],
}

for person,places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are as follows:")
    for place in places:
        print(f"{place.title()}")