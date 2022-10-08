N,INF=310,0x3f3f3f3f
f=[[INF]*N for _ in range(N)]
n=int(input())
w=[0]+[int(x) for x in input().split()]
for i in range(1,n+1):
    w[i],f[i][i]=w[i]+w[i-1],0

for d in range(2,n+1):
    for i in range(1,n+1):
        if i+d-1>n:break
        l,r=i,i+d-1
        for k in range(l,r):
            f[l][r]=min(f[l][r],f[l][k]+f[k+1][r]+w[r]-w[l-1])

print(f[1][n])



