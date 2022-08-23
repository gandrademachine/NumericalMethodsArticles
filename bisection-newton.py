import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def f(x):
    h2 = 0.0e0
    return x*np.tan(x) - h2

def dfdx(x):
    return np.tan(x)+ x / np.cos(x)**2
def bisectionMethod(a,b,n, err, table, k = 0 ):
    # print(f"a={a}, b={b}")
    x0 = (a+b)/2
    table.append([x0, f(x0), k])
    if (b-x0 < err) or (x0-a < err) or n == 0 or f(x0) == 0:
        print("Bisection Method:")
        print(tabulate(table, headers=['xk', 'f(xk)', 'k'], tablefmt='orgtbl'))
    else:
        k += 1
        if f(b) * f(x0) < 0:
            a = x0
            bisectionMethod(a,b, n-1, err, table, k)
        else:
            b = x0
            bisectionMethod(a,b, n-1, err, table, k)

def newtonMethod(x0, n, err, table, k = 0):
    x = x0 - f(x0)/dfdx(x0)
    table.append([x0, f(x0), dfdx(x0), k])
    if (abs(x-x0) < err) or n == 0 :
        print("Newton Method")
        print(tabulate(table, headers=['x{k}', 'f(x{k})', 'f\'(x{k})', 'k'], tablefmt='orgtbl'))
    else:
        x0  = x
        k += 1
        newtonMethod(x0, n-1, err, table, k)

a = 14
b = 16
x0 =  16
n = 100
err = 1e-4
btable = []
ntable = []
bisectionMethod(a, b, n, err, btable)
newtonMethod(x0, n, err, ntable)
