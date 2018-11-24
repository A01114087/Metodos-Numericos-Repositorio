# Metodo Euler
#y' - e^x = 0, y(0) = 1, y(5) = ?
# dy/dx = e^x

import math
import numpy as np
import matplotlib.pyplot as plt



def f(x,y):
    return math.exp(x)

def euler(y0,x,h,f):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h*f(x[i-1],y[i-1]))
    return y

n = 6
a = 0
b = 5
h = abs(a-b)/(n-1)
print (h)
x = np.linspace(a,b,n)
print (x)
y = euler(1,x,h,f)

plt.plot(x,y,'g')
plt.plot(x,[math.exp(xi) for xi in x], 'b')
plt.grid()
