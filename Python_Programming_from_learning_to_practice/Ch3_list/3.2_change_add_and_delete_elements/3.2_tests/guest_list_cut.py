#向哲煜 2023.12.24
guest_list = ['mom', 'dad', 'grandpa', 'grandma', 'bro']

print(f"Can you have a meal with me, {guest_list[0]}?")
print(f"Can you have a meal with me, {guest_list[1]}?")
print(f"Can you have a meal with me, {guest_list[2]}?")
print(f"Can you have a meal with me, {guest_list[3]}?")
print(f"Can you have a meal with me, {guest_list[4]}?")

print(f"\nGreat!I find a bigger table.\n")

guest_list.insert(0, 'homie')
guest_list.insert(2, 'schoolmate')
guest_list.append('friend')

print(f"Can you have a meal with me, {guest_list[0]}?")
print(f"Can you have a meal with me, {guest_list[1]}?")
print(f"Can you have a meal with me, {guest_list[2]}?")
print(f"Can you have a meal with me, {guest_list[3]}?")
print(f"Can you have a meal with me, {guest_list[4]}?")
print(f"Can you have a meal with me, {guest_list[5]}?")
print(f"Can you have a meal with me, {guest_list[6]}?")
print(f"Can you have a meal with me, {guest_list[7]}?")

print(f"\nOh no!My new table cannot be delivered in time.I can only invite 2 people then.\n")

apology = guest_list.pop()
print(f"Sorry {apology.title()}")
apology = guest_list.pop()
print(f"Sorry {apology.title()}")
apology = guest_list.pop()
print(f"Sorry {apology.title()}")
apology = guest_list.pop()
print(f"Sorry {apology.title()}")
apology = guest_list.pop()
print(f"Sorry {apology.title()}")
apology = guest_list.pop()
print(f"Sorry {apology.title()}")

print(f"{guest_list[0].title()},you are still invited.")
print(f"{guest_list[1].title()},you are still invited.")

del guest_list[1]
del guest_list[0]

print(guest_list)