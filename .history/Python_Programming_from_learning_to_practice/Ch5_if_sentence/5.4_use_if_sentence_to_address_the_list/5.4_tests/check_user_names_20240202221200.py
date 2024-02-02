# 向哲煜 2024.2.2

current_users = ['jack', 'john', 'tom', 'rose', 'alice']
new_users = ['jack', 'john', 'mary', 'frank', 'nero']

current_users_copy = []

for current_user in current_users:
    current_users_copy.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print("This name has already been used!")
    else:
        print("")