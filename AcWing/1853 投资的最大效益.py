N,M=1000010,101
f,a,b=[0]*N,[0]*M,[0]*M
s,n,d=map(int,input().split())
for i in range(1,d+1):
    a[i],b[i]=map(int,input().split())

for k in range(n):
    for i in range(1,d+1):
        for j in range(a[i],s+1):
            f[j]=max(f[j],f[j-a[i]]+b[i])
    s+=f[s]

print(s)
