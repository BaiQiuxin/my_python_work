# 向哲煜 2024.3.31

from random import choice

prize = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

choose = f"{choice(prize)}{choice(prize)}{choice(prize)}{choice(prize)}"

my_ticket = []

ticket =f"{choice(prize)}{choice(prize)}{choice(prize)}{choice(prize)}"

while ticket != choose:
    my_ticket.append(ticket)
    ticket =f"{choice(prize)}{choice(prize)}{choice(prize)}{choice(prize)}"

print(my_ticket.)