import sympy as sy

x = sy.symbols('x')
f = sy.log((1 + x), 2) * sy.exp(-x)
print(sy.integrate(f, (x, 0, sy.oo)).evalf())
print(sy.log(1.14142, 2).evalf())
