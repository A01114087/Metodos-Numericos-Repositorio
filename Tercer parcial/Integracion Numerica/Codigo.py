import matplotlib.pyplot as plt

import math



x = [200,400,500,700,900,1000]

y = [60,120,150,210,260,290]

n = 6

plt.plot(x, y, 'ro')

plt.show()



sumx = sum(x)

sumy = sum(y)

sumx2 = sum( xi * xi for xi in x  )

sumxy = sum ( xi * yi for xi, yi in zip(x,y) )



m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))

b = (sumy/n) - (m * (sumx/n))



print(m,b)



# Ejemplo 2 regresion con parabola

x = [0.001,1,2,3,4,5]

y = [2.1,7.7,13.6,27.2,40.9,61.1]

n = 6

plt.plot(x, y, 'ro')

plt.show()

logx = [math.log10(xi) for xi in x]

logy = [math.log10(yi) for yi in y]

x = logx

y = logy



sumx = sum(x)

sumy = sum(y)

sumx2 = sum( xi * xi for xi in x  )

sumxy = sum ( xi * yi for xi, yi in zip(x,y) )



m = (sumxy - (sumx*sumy/n))/(sumx2 - (sumx*sumx/n))

b = (sumy/n) - (m * (sumx/n))

alpha = 10**b

beta = m



print ("alpha, beta",alpha,beta)
