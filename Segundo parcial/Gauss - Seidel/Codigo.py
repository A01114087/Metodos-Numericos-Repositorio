# Gauss-seidel
# x1 + x2 + x3 = 16
# -2.25x1 - 1.5x2 + x3 = 16.5
# 4x1 + 2x2 + x3 = 16

def getX1(x2,x3):
    return (x3)/2

def getX2(x1,x3):
    return (210-15*x1-5*x3)/20

def getX3(x1,x2):
    return (2*x1-3*x2)



x1 = 0
x2 = 0
x3 = 0
E = 0.01

for i in range(100):
   x1i = getX1(x2,x3)
   x2i = getX2(x1i,x3)
   x3i = getX3(x1i,x2i)
   Ex1 = abs(x1-x1i)
   Ex2 = abs(x2-x2i)
   Ex3 = abs(x3-x3i)
   x1 = x1i
   x2 = x2i
   x3 = x3i
   if Ex1 < E and Ex2 < E and Ex3 < E:
      break
print("La solucion es ",x1,x2,x3)
