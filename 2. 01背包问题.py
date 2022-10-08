M=1010
N,V=map(int,input().split())
f,v,w=[0]*M,[0]*M,[0]*M
for i in range(1,N+1):
    v[i],w[i]=map(int,input().split())
for i in range(1,N+1):
    for j in range(V,v[i]-1,-1):
        f[j]=max(f[j],f[j-v[i]]+w[i])
print(f[V])
    
    
    
