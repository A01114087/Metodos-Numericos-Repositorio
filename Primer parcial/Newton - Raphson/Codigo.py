def f(x):
    return 2*x**2 - 5*x + 3

def fprima(x):
    return 4*x - 5
    
x0 = 2
itera = 0
for i in range (100):
    itera += 1
    xr = x0 - f(x0)/fprima(x0)
    if abs(f(xr)) < 0.0001:
        break
    x0 = xr
    
print ("La raiz es %.5f"%x0)
print ("Usando %i iteraciones"%itera)
    
