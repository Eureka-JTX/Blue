N,null=210,0x3f3f3f3f
def flyod():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])

n,m,k=map(int,input().split())
g=[[null]*N for _ in range(N)]
for _ in range(m):
    x,y,z=map(int,input().split())
    g[x][y]=min(g[x][y],z)
for _ in range(k):
    x,y=map(int,input().split())
    flyod()
    if g[x][y]>(null/2):    print("impossible")
    else:   print(g[x][y])

           
