import sympy as sp

def sqrt_func(x):
    print(f"the square root of number {x} is {sp.sqrt(x)}")

x,y,z = sp.symbols('x y z')
sp.init_printing(use_unicode=True)
print(sp.diff(sp.sin(x)*sp.exp(x),x))
