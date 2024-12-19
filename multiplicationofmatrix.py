#Matrix multiplication
r, c = map(int,input().split())
def inputMat(r,c):
    mat =[]
    mat = [[int(input()) for j in range(c)] for i in range(r)]
    print(mat)
    return mat
def printMat(mat):
    r = len(mat)
    for i in range(r):
        c= len(mat[i])
        for j in range(c):
            print(mat[i][j],end=" ")
        print()

def mulMat(m1,m2):
    m3=[]
    for i in range(len(m1)):
        c =[]
        for j in range(len(m2)):
            val=0
            for k in range(len(m2)):
                val+=m1[i][k]*m2[k][j]
            c.append(val)
        m3.append(c)   
    return m3
    

mat1  = inputMat(r,c)
mat2  = inputMat(r,c)
print("Matrix Mat1")
printMat(mat1)
print("Matrix Mat2")
printMat(mat2)
mat3 =mulMat(mat1,mat2)
print("Matrix Mat3")
printMat(mat3)