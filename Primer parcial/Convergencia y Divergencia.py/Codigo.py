import matplotlib.pyplot as plt
import numpy as np

def xnew(x):
    return (2*x**2+3)/5

x0 = 0
x1 = 0
itera = 0
x0array = np.zeros(100)
x1array = np.zeros(100)
xexe = np.zeros(100)

for i in range(100):
    x1 = xnew(x0)
    xexe[i]=i
    x0array[i] = x0
    x1array[i] = x1
    if abs(x1-x0) < 0.001:
        break
        
    x0 = x1     
    itera += 1
    
plt.plot(xexe,x0array,x1array)
plt.grid()

print ("La raiz es %.5f"%x1)
print ("usando %d iteraciones"%itera)
