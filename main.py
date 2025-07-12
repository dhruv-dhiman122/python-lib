import sympy as sp
from sympy import log
from sympy import tan,cos,sin
"""
for anyone seeing this, plz ingore this file because i am using this
for learning new library for my project, there is nothing for you in this file.
I made this file so that i get used to pushing the code to github
"""
sp.init_printing(use_unicode=True)
sp.init_printing()
x,y,z = sp.symbols('x y z')
a,b,c = sp.symbols('a b c')
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
#trigosimp
print(f"this is using trigsimp function {sp.trigsimp(exp)}")
#expanding the trig
print(f"this is unsing expand trig function {sp.expand_trig(exp)}")
#powsimp
print(f"this is using power simply function {sp.powsimp(exp3,force=True)}")
#exapnd power exp
print(f"this is expanding power expnont version {sp.expand_power_exp(x**(a+b))}")
#expanding the base
print(f"this is expanding power base version {sp.expand_power_base((x*y)**a)}")
#powdenest
print(f"this is function called powdenest {sp.powdenest((x**a)**b,force=True)}")
# adding stmobols
x,y = sp.symbols('x y',positive=True)
n = sp.symbols('n',real=True)
#we are expanding log
print(f"we are expanding the logrithm {sp.expand_log(sp.log(x*y))}")
#we are expanding log
print(f"We are expanding the logrithm {sp.expand_log(sp.log(x/y))}")
#we are expanding log
print(f"We are expanding the logrithm {sp.expand_log(sp.log(z**2),force=True)}")
#we are combining the log
print(f"We can combine different algorithm {sp.logcombine(log(x)+log(y))}")
#we are factorial
print(f"We can doing factorial function {sp.factorial(4)}")
#we are doing bionomial
print(f"We are doing bionomial function {sp.binomial(3,10)}")
print(f"We are writing the gamma function {sp.gamma(8)}")
# we are making the generalized hypergeometric function 
print(f"We are making generalized hypergeometric function{sp.hyper([1,2,3],[4],z)}")
#we are rewriting an expression into another version of function
print(f"we are rewriting the function of tan in cos {tan(x).rewrite(cos)}")
#we are trying to expand a function 
print(f"We are expanding the fucntion {sp.expand_func(sp.gamma(x+3))}")
#we are using hyperexpand function
print(f"We are using expand function {sp.hyperexpand(sp.hyper([1,2,3],[4],z))}")
#we are adding interger 
a,b,c = sp.symbols('a b c',interger=True)
expr = sp.factorial(x)/sp.factorial(x+1)
print(f"We are simplying the expr {sp.combsimp(expr)}")
expr2 = sp.gamma(x+1)/sp.gamma(x+2)
#we are simplying the gamma function
print(f"We are simplying the gamma function {sp.gammasimp(expr2)}")
"""
From here i am learning about calculus usage function
"""
print(f"We can differentatie the function {sp.diff(x**4,x)}")
#we can call differentate function with other method
print(f"We can make another differenatate function {expr.diff(x,2)}")
# we are integrating the function given
print(f"We can integrate function {sp.integrate(cos(x),x)}")
# we adding now the limit to the integrate
print(f"We will be adding the limit to the integrate {sp.integrate(cos(x),(x,0,1))}")
# we are integrating the function of two variable
func = sp.exp(x**2-y**2)
print(f"We are integrating two different function with limit {sp.integrate(func,(x,0,1),(y,0,1))}")
# we will integrate a numerical function with two vairable
print(f"We are integrating function with two different {sp.integrate(sp.sqrt(2)*x,(x,0,1))}")
#we are using limit function
print(f"We are using limit function {sp.limit(func,x,6)}")
#we will now solve the limit function
func1 = sp.limit(sp.cos(x-1)/x,x,9)
print(f"we will use the do it function {func1.doit()}")
