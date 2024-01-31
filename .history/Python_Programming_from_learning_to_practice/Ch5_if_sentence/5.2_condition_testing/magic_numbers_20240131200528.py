# 向哲煜 2024.1.21

#数值比较
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That's not the correct answer.Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# 检查多个条件

#用and检查多个条件

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print( (age_0 >= 21) and (age_1 >= 21) )