import sympy as sp

def sqrt_func(x):
    print(f"the square root of number {x} is {sp.sqrt(x)}")

user_num = int(input("Enter the number you want a square root of "))
sqrt_func(user_num)
