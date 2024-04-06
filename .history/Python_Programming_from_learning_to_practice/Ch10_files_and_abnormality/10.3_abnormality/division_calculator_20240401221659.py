# 向哲煜 2024.4.1

print("Please give me two numbers, and I;ll divide them.")
print("Enter'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number/second_number)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")