def xnew(x):
    return (2*x**2+3)/5

x0 = 0
x1 = 0
itera = 0

for i in range(100):
    x1 = xnew(x0)
    if abs(x1-x0) < 0.001:
        break
        
    x0 = x1     
    itera += 1
    
print ("La raiz es %.5f"%x1)
print ("usando %d iteraciones"%itera)
