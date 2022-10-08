M=10000010
V,N=map(int,input().split())
f,v,w=[0]*M,[0]*M,[0]*M
for i in range(1,N+1):
    v[i],w[i]=map(int,input().split())
for i in range(1,N+1):
    for j in range(v[i],V+1):
        f[j]=max(f[j],f[j-v[i]]+w[i])
print(f[V])
