# 2*x1 + 4*x2 - x3 = -5
# x1 + x2 - 3*x3 = -9
# 4*x1 + x2 +2*x3 = 9

#Operaciones de Matrices
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


####### Factorizacion LU #######


U = createMatriz(3,3,0)
U[0] = [1,1,1]
U[1] = [1,-1,0]
U[2] = [-1,0,1]

L = createMatriz(3,3,0)
L[0] = [1,0,0]
L[1] = [0,1,0]
L[2] = [0,0,1]

C = createMatriz(3,1,0)
C[0] = [20]
C[1] = [-5]
C[2] = [-4]

for i in range(3):
    if U[i][i] == 0:
        print("La matriz no tiene LU")
        break
    for j in range(i+1,3):
        c = -1*U[j][i]/U[i][i]
        L[j][i] = -1*c
        for k in range(3):
            U[j][k] += c*U[i][k]
print(U)
print(L)

#### LZ = C #####
Z = createMatriz(3,1,0)
for i in range(3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j] * Z[j][0]
print(Z)

###### UB = Z ######

B = createMatriz(3,1,0)
for i in range(2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            break
        B[i][0] -= U[i][j] * B[j][0]
    B[i][0] = B[i][0]/U[i][i]
print(B)
