import sympy as sp

sp.init_printing(use_unicode=True)

x,y,z = sp.symbols('x y z')
mat = x + 1
print(mat.subs(x,2))
