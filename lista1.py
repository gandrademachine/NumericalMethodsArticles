import numpy as np
import matplotlib.pyplot as plt

# Data

T0 = 180
Tn = 65
Tamb = 20
D = np.round(3.5 * 1e-5,11)
h = 150
L = 0.15
k = 120
node = 1000
area = np.pi * D**2/4
P = np.pi * D
dx = L/node
m2 = np.round(h*P/(k*area), 6)  
print(m2)
x = np.linspace(0, L, node + 1)
A = np.zeros((node + 1, node + 1))


b = -Tamb * np.ones(node + 1) * m2
b[0] = 180
b[-1] = 65 
for i in range(node + 1):
    A[i][i] = -(2 / dx**2 + m2)
    if i == 0:
        A[i][i] = 1
    elif i == node:
        A[i][i] = 1
    else:
        A[i][i+1] = 1 / dx**2
        A[i][i-1] = 1 / dx**2

u = np.linalg.inv(A) @ b
print(u)
v = np.linalg.solve(A,b)
plt.title(f"T0:{T0}, Tn:{Tn}, Tam:{Tamb}, D:{D}, h:{h}, L:{L}, k:{k}")
plt.plot(x, u)
plt.plot(x, v)
plt.xlim(x[0], x[-1])
# plt.ylim(0, 5)
plt.xlabel("bar position(m)")
plt.ylabel("Temperature (ºC)")
plt.grid()
plt.show()
