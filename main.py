import sympy as sp

def sqrt_func(x):
    print(f"the square root of number {x} is {sp.sqrt(x)}")

x,y,z = sp.symbols('x y z')
sp.init_printing(use_unicode=True)
exp = sp.integrate(sp.sin(x**2), (x, -sp.oo, sp.oo))
print(exp)
