# Сделать в самой функции проверку на условие умножение и тд!!!!!!!!
def fillingArray(row, col, list, A):
    k = 0
    for i in range(row):
        for j in range(col):
            A[i][j] = list[k]
            k += 1


def matr(N=1, M=1, a=0):
    sp = []
    # if N != 1 and M == 1:
    #     M = N
    for i in range(N):
        sp.append([a] * M)
    return sp


def subOfMatrix(A, B):
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])):
        resMatrix = matr(len(A), len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                resMatrix[i][j] = A[i][j] - B[i][j]
        return resMatrix
    else:
        return False


def sumOfMatrix(A, B):
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])):
        resMatrix = matr(len(A), len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                resMatrix[i][j] = A[i][j] + B[i][j]
        return resMatrix
    else:
        return False


def varMultiplyMatrix(var, A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= var
    return A


def multiplyOfMatrix(A, B):
    if len(A[0]) == len(B):
        s = 0
        t = []
        res = []
        rowA = len(A)
        colA = len(A[0])
        rowB = colA
        colB = len(B[0])
        for z in range(0, rowA):
            for j in range(0, colB):
                for i in range(0, colA):
                    s = s + A[z][i] * B[i][j]
                t.append(s)
                s = 0
            res.append(t)
            t = []
        return res
    else:
        return False


def transposeMatrix(A):
    res = []
    n = len(A)
    m = len(A[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [A[i][j]]
        res = res + [tmp]
    return res


fin = open("input.txt")
fout = open("output.txt", "w")
listOfAB = list(fin.readline().split())
alpha = float(listOfAB[0])
Beta = float(listOfAB[1])
listOfRowColA = list(fin.readline().split())
RowA = int(listOfRowColA[0])
ColA = int(listOfRowColA[1])
listOfVarMatrixA = list(fin.readline().split())
for i in range(len(listOfVarMatrixA)):
    listOfVarMatrixA[i] = float(listOfVarMatrixA[i])
MatrixA = matr(RowA, ColA)
fillingArray(RowA, ColA, listOfVarMatrixA, MatrixA)
listOfRowColB = list(fin.readline().split())
RowB = int(listOfRowColB[0])
ColB = int(listOfRowColB[1])
listOfVarMatrixB = list(fin.readline().split())
for i in range(len(listOfVarMatrixB)):
    listOfVarMatrixB[i] = float(listOfVarMatrixB[i])
MatrixB = matr(RowB, ColB)
fillingArray(RowB, ColB, listOfVarMatrixB, MatrixB)

listOfRowColC = list(fin.readline().split())
RowC = int(listOfRowColC[0])
ColC = int(listOfRowColC[1])
listOfVarMatrixC = list(fin.readline().split())
for i in range(len(listOfVarMatrixC)):
    listOfVarMatrixC[i] = float(listOfVarMatrixC[i])
MatrixC = matr(RowC, ColC)
fillingArray(RowC, ColC, listOfVarMatrixC, MatrixC)

listOfRowColD = list(fin.readline().split())
RowD = int(listOfRowColD[0])
ColD = int(listOfRowColD[1])
listOfVarMatrixD = list(fin.readline().split())
for i in range(len(listOfVarMatrixD)):
    listOfVarMatrixD[i] = float(listOfVarMatrixD[i])
MatrixD = matr(RowD, ColD)
fillingArray(RowD, ColD, listOfVarMatrixD, MatrixD)

listOfRowColF = list(fin.readline().split())
RowF = int(listOfRowColF[0])
ColF = int(listOfRowColF[1])
listOfVarMatrixF = list(fin.readline().split())
for i in range(len(listOfVarMatrixF)):
    listOfVarMatrixF[i] = float(listOfVarMatrixF[i])
MatrixF = matr(RowF, ColF)
fillingArray(RowF, ColF, listOfVarMatrixF, MatrixF)

test = 1
t = 1
while test == 1 and t == 1:
    firstAct = varMultiplyMatrix(alpha, MatrixA)
    secondAct = transposeMatrix(MatrixB)
    thirdAct = varMultiplyMatrix(Beta, secondAct)
    fourthAct = sumOfMatrix(firstAct, thirdAct)
    if fourthAct == False:
        test = 0
        break
    fifthAct = transposeMatrix(fourthAct)
    sixthAct = multiplyOfMatrix(MatrixC, fifthAct) #
    if sixthAct == False:
        test = 0
        break
    seventhAct = multiplyOfMatrix(sixthAct, MatrixD) #
    if seventhAct == False:
        test = 0
        break
    resAct = subOfMatrix(seventhAct, MatrixF)
    if resAct == False:
        test = 0
        break
    t = 0
if test != 0:
    print(1, file=fout)
    print(len(resAct), len(resAct[0]), file=fout)
    for i in range(len(resAct)):
        for j in range(len(resAct[0])):
            print(resAct[i][j], end=" ", file=fout)
if test == 0:
    print(0, file=fout)
