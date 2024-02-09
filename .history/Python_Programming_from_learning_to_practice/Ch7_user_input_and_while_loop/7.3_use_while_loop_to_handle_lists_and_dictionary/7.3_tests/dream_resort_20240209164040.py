# 向哲煜 2024.2.9

dream_places = {}
prompt_name = "What is your name?"
prompt_place = "If you could visit one place in the world,where would you go? "

polling_active = True

while polling_active:
    name = input(prompt_name)
    place = input(prompt_place)
    dream_places[name] = place
    
    repeat = input("Would you like another person to respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False

