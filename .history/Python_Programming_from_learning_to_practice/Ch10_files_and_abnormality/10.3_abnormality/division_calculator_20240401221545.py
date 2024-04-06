# 向哲煜 2024.4.1

print("Please give me two numbers, and I;ll divide them.")
print("Enter'q' to quit.")

while True:
    first_number = input("\nFirst number: ")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")