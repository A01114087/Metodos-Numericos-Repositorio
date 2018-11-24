import numpy as np
import matplotlib.pyplot as plt

def y(x):
  return 2*x**2 - 5*x + 3

xarray = np.linspace(0,2,100)
yarray = np.zeros(len(xarray))

for i in range (len(xarray)):
    yarray[i]=y(xarray[i])

plt.plot(xarray,yarray)
plt.grid()
