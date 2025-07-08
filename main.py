import sympy as sp

sp.init_printing(use_unicode=True)

x,y,z = sp.symbols('x y z')
exp = (x*2)**2+x*y*(4*y)
exp2 = x**y
print(exp2.subs(y,x**(x**x)))
