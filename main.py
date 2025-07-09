import sympy as sp

sp.init_printing(use_unicode=True)
sp.init_printing()
x,y,z = sp.symbols('x y z')
#using subs
exp = sp.sin(2*x) + sp.cos(2*x)
exp2 = x**y
exp3 =  (x*2)**2+((2*x)+(2*y))**2
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

#simplify function
print(f"this is due to simplify function {sp.simplify(x**2+2*x+1)}")
#factor fucntion
print(f"this is due to factor function {sp.factor(x**2+2*x+1)}")
#expand function
print(f"this is exapand function {sp.expand(exp)}")
#collect function
print(f"this is collect function {sp.collect(exp3,x)}")
#coeff function
print(f"this is coeff function {exp3.coeff(x,2)}")
#cancel function
print(f"the is cancel function {sp.cancel((x**2+2*x+1)/(x**2+x))}")
#inverse trigo
print(f"this is inverse function {sp.asin(1)}")
