import sympy as sp

sp.init_printing(use_unicode=True)
sp.init_printing()
x,y,z = sp.symbols('x y z')
#using subs
exp = sp.sin(2*x) + sp.cos(2*x)
exp2 = x**y
print(exp2.subs(y,x**(x**x)))
print(exp.subs(sp.sin(2*x),2*sp.sin(x)*sp.cos(x)))
#using evalf
exp = sp.sqrt(8)
print(exp.evalf())
#combining evalf and subs
print(exp.evalf(subs={x:4.4}))
#function of printing stuff
#sp.init_session(quiet=True)

#code for simplification section

print(f"this is due to simplify function {sp.simplify(x**2+2*x+1)}")
print(f"this is due to factor function {sp.factor(x**2+2*x+1)}")

