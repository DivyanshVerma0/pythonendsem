#transpose
def inputmat(r,c):
    mat=[]
    for i in range(r):
        arr=[]
        for j in range(c):
            n=int(input())
            arr.append(n)
        mat.append(arr)
    return mat
def printmat(m):
    r=len(m)
    for i in range(r):
        c=len(m[i])
        for j in range(c):
            print(m[i][j],end=" ")
        print()
r,c=map(int,input().split())      
mat1=inputmat(r,c)
printmat(mat1)
for i in range(r):
    for j in range(c):
        t2=mat1[j][i]
        print(t2,end=" ")
    print()