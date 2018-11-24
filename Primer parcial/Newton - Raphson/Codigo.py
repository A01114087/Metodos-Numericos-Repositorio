## Funciones para matrices

def createMatriz(m,n,v):

    C = []

    for i in range(m):

        C.append([])

        for j in range(n):

            C[i].append(v)

    return C



def getDimensiones(A):

    return (len(A),len(A[0]))



def sumMatrices(A,B):

    Am,An = getDimensiones(A)

    Bm,Bn = getDimensiones(B)

    if Am != Bm or An != Bn:

        print("Las dimensiones son diferentes")

        return []

    C = createMatriz(Am,An,0)

    for i in range(Am):

        for j in range(An):

            C[i][j] = A[i][j] + B[i][j]

    return C



def restaMatrices(A,B):

    Am,An = getDimensiones(A)

    Bm,Bn = getDimensiones(B)

    if Am != Bm or An != Bn:

        print("Las dimensiones son diferentes")

        return []

    C = createMatriz(Am,An,0)

    for i in range(Am):

        for j in range(An):

            C[i][j] = A[i][j] - B[i][j]

    return C



def mulMatrices(A,B):

    Am,An = getDimensiones(A)

    Bm,Bn = getDimensiones(B)

    if An != Bm:

        print("Las matrices no son conformables")

        return []

    C = createMatriz(Am,Bn,0)

    for i in range(Am):

        for j in range(Bn):

            for k in range(An):

                C[i][j] += A[i][k] * B[k][j]

    return C

def getMenorMatriz(A,r,c):

    m,n = getDimensiones(A)

    C = createMatriz(m-1,n-1,0)

    for i in range(m):

        if i == r:

            continue

        for j in range(n):

            if j == c:

                continue

            Ci = i

            if i > r:

                Ci = i - 1

            Cj = j

            if j > c:

                Cj = j -1

            C[Ci][Cj] = A[i][j]

    return C



def detMatriz(A):

    m,n = getDimensiones(A)

    if m != n:

        print("La matriz no es cuadrada")

        return -1

    if m == 1:

        return m

    if m == 2:

        return  A[0][0]*A[1][1] - A[0][1]*A[1][0]

    det = 0

    for j in range(n):

        det += (-1)**(j)*A[0][j]*detMatriz(getMenorMatriz(A,0,j))

    return det



def getMatrizAdyacente(A):

    m,n = getDimensiones(A)

    C = createMatriz(m,n,0)

    for i in range(m):

        for j in range(n):

            C[i][j] = (-1)**(i+j)*detMatriz(getMenorMatriz(A,i,j))

    return C



def getMatrizTranspuesta(A):

    m,n = getDimensiones(A)

    C = createMatriz(n,m,0)

    for i in range(m):

        for j in range(n):

            C[j][i] = A[i][j]

    return C



def getMatrizInversa(A):

    detA = detMatriz(A)

    if detA == 0:

        print("La matriz no tiene inversa")

        return 0

    At =  getMatrizTranspuesta(A)

    adyAt =  getMatrizAdyacente(At)

    m,n = getDimensiones(A)

    C = createMatriz(m,n,0)

    for i in range(m):

        for j in range(n):

            C[i][j] = (1/detA)*adyAt[i][j]

    return C



####

# Sistema a resolver

# a**2 + b**2 = 10**2

# a * b = 40



####

# Esta parte se debe cambiar y corresponde

# Al sistema a resolver

def u(x,y,z,k):

    return x + y - 10



def v(x,y,z,k):

    return (x * y) - 40


def m(x,y,z,k):

    return (x * y) - 40


def n(x,y,z,k):

    return (x * y) - 40


def dudx(x,y,z,k):

    return y



def dudy(x,y,z,k):

    return x



def dvdx(x,y):

    return 2*x



def dvdy(x,y):

    return 2*y





###

#Esta es la matriz Jacobiana

# Corresponde a las derivadas parciales

A = [[dudx, dudy],[dvdx, dvdy]]

###

# Esta es una matriz con las funciones originales

D = [[u],[v]]



####

#Valores iniciales

C = [[8],[5]]

####

# Error deseado

E = 0.001



for i in range(100):

    Am,An = getDimensiones(A)

    ## Calcular D en el punto C

    Di =createMatriz(Am,1,0)

    for k in range(Am):

        for j in range(1):

            Di[k][j] = D[k][j](C[0][0],C[1][0])

    Ai = createMatriz(Am,An,0)

    for k in range(Am):

        for j in range(An):

            Ai[k][j] = A[k][j](C[0][0],C[1][0])

    invAi = getMatrizInversa(Ai)

    Bi = restaMatrices(C,mulMatrices(invAi,Di))

    Ce = restaMatrices(C,Bi)

    if abs(Ce[0][0]) < E and abs(Ce[1][0]) < E:

        C = Bi

        break

    C = Bi



print("Los valores son",C)

print("U", u(C[0][0],C[1][0]))

print("v", v(C[0][0],C[1][0]))
