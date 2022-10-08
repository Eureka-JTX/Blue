def C1(a,b):
    res=1
    while a:
        res*=b/a
        b-=1
        a-=1
    return int(res)

def C2(a,b):
    for i in range(N):
        for j in range(i+1):
            if not j:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j]+c[i-1][j-1]
    return c[a][b]

N=10
c=[[0]*N for _ in range(N)]
print(C1(2,5))
print(C2(5,2))
