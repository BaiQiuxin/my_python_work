# 向哲煜 2024.4.1

print("Please type two numbers, and I'l tell you their sum.")
print("Enter 'q' to quit.")


while True:
    first_number = input("First number: ")
    if first_number == 'p':
        break
    second_number = input("Second number: ")
    if second_number == 'p':
        break
    
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print(f"{first_number} + {se}")