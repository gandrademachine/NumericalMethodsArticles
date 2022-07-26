import numpy as np
import matplotlib.pyplot as plt

# Data

T0 = 180
Tn = 65
Tamb = 20
D = 3.5 * 1e-3
h = 150
L = 0.15
k = 120
node = 100
dx = 1e-3
x = np.linspace(0, L, node)
A = np.zeros((node, node))

def g(x):
    return (4* h) * (x - Tamb) / (k*D)

b = np.array([g(i) for i in x]) 

b[0] = 180
b[-1] = 65

for i in range(node):
    A[i][i] = -2 / dx**2
    if i == 0:
        A[i][i+1] = 1 / dx**2
    elif i == node - 1:
        A[i][i-1] = 1 / dx**2
    else:
        A[i][i+1] = 1 / dx**2
        A[i][i-1] = 1 / dx**2

u = A @ b
print(u)
plt.plot(x, u)
plt.show()
