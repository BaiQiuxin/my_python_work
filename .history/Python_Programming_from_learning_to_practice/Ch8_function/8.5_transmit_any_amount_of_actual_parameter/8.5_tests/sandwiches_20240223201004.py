# 向哲煜 2024.2.23

def make_sandwich(*ingredients):
    """概述顾客想要的三明治"""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('cheese')
make_sandwich('ham', 'beacon')
make_sandwich('egg', 'cheese', '')