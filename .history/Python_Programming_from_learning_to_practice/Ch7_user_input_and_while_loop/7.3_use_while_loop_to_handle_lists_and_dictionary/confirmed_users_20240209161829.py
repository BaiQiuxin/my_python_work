# 向哲煜 2024.2.9

#在列表之间移动元素
#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users =['alice', 'brian', 'candace']
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的用户都移动到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(confirmed_users)