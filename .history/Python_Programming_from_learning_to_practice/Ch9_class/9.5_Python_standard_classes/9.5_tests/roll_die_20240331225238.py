# 向哲煜 2024.3.31

from die import Die

roll = 1

while roll <= 10:
    my_die = Die()
    my_die.roll_die()

    my_die = Die(10)
    my_die.roll_die()

    my_die = Die(20)
    my_die.roll_die()
