M=110
f,s,v,w=[0]*M,[0]*M,[[0]*M for _ in range(M)],[[0]*M for _ in range(M)]
N,V=map(int,input().split())
for i in range(1,N+1):
    s[i]=int(input())
    for j in range(1,s[i]+1):
        v[i][j],w[i][j]=map(int,input().split())

for i in range(1,N+1):
    for j in range(V,-1,-1):
        for k in range(1,s[i]+1):
            if v[i][k]<=j:
                f[j]=max(f[j],f[j-v[i][k]]+w[i][k])

print(f[V])
        
        
        
    
