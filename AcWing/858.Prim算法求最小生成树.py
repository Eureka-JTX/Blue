N,null=510,0x3f3f3f3f
g=[[null]*N for _ in range(N)]
dist,st=[null]*N,[False]*N

def prim():
    dist[1],res=0,0
    for _ in range(n):
        t=-1
        for i in range(1,n+1):
            if not st[i] and(t==-1 or dist[t]>dist[i]):
                t=i
        if dist[t]==null:    return 'impossible'
        else:   res+=dist[t]
        st[t]=True
        for i in range(1,n+1):
            dist[i]=min(dist[i],g[t][i])
    return res

n,m=map(int,input().split())
for _ in range(m):
    u,v,w=map(int,input().split())
    g[u][v]=g[v][u]=min(g[u][v],w)
print(prim())
   
