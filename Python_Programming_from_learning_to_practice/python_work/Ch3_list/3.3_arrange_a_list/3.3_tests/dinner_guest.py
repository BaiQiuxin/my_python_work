#向哲煜 2023.12.27
guest_list = ['mom', 'dad', 'grandpa', 'grandma', 'bro']

print(f"Can you have a meal with me, {guest_list[0]}?")
print(f"Can you have a meal with me, {guest_list[1]}?")
print(f"Can you have a meal with me, {guest_list[2]}?")
print(f"Can you have a meal with me, {guest_list[3]}?")
print(f"Can you have a meal with me, {guest_list[4]}?")

print(f"\nToo bad {guest_list[4]} cannot come\n")

guest_list[4] = 'homie'

print(f"Can you have a meal with me, {guest_list[0]}?")
print(f"Can you have a meal with me, {guest_list[1]}?")
print(f"Can you have a meal with me, {guest_list[2]}?")
print(f"Can you have a meal with me, {guest_list[3]}?")
print(f"Can you have a meal with me, {guest_list[4]}?")

total_number = len(guest_list)
print(f"There are {total_number} guests in total.")