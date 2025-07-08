import sympy as sp

sp.init_printing(use_unicode=True)

x,y,z = sp.symbols('x y z')
exp = sp.sin(2*x) + sp.cos(2*x)
exp2 = x**y
print(exp2.subs(y,x**(x**x)))
print(exp.subs(sp.sin(2*x),2*sp.sin(x)*sp.cos(x)))
