# Eliminacion Gaussiana: Ya que no se pudo Gauss-Seidel #8
# 2x1 + 0 - x3 = 0
# 2x1 + 3x2 - x3 = 0
# 15x1 + 20x2 + 5x3 = 210

def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

MA= createMatriz(3,4,0)
MA[0] = [2,0,-1,0]
MA[1] = [2,3,-1,0]
MA[2] = [15,20,5,210]

MAm = 3
MAn = 4
for i in range(MAm):
    pivote = MA[i][i]
    if pivote == 0:
        for j in range(i+1,MAm):
            pivote=MA[j][i]
            if pivote !=0:
                T=MA[i]
                MA[i]=MA[j]
                MA[j]=T
                break
    for k in range(MAn):
        MA[i][k] = (1/pivote)*MA[i][k]
    for j in range(i+1,MAm):
        c = -1*MA[j][i]
        T = createMatriz(1,MAn,0)
        for k in range(MAn):
            T[0][k] = c*MA[i][k]
        for k in range(MAn):
            MA[j][k] += T[0][k]
print("EG",MA)
B = createMatriz(3,1,0)
for i in range(MAm-1,-1,-1):
    B[i][0] = MA[i][MAn-1]
    for j in range(MAn-2,-1,-1):
        if i == j:
            break
        B[i][0] -= MA[i][j] * B[j][0]
print(B)
