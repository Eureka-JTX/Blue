N=510
null=0x3f3f3f3f
dist=[null]*N
st=[False]*N

def dijkstra():
    dist[1]=0
    for _ in range(n):
        t=-1
        for i in range(1,n+1):
            if not st[i] and (t==-1 or dist[t]>dist[i]):
                t=i
        st[t]=True
        for i in range(1,n+1):
            dist[i]=min(dist[t]+g[t][i],dist[i])
    return dist[n] if dist[n] else -1

def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])

def prim():
    dist[1],res=0,0
    for _ in range(n):
        t=-1
        for i in range(1,n+1):
            if not st[i] and(t==-1 or st[t]>st[i]):
                t=i
        if dist[t]=null:    return 'imp'
        else:   res+=dist[t]
        st[t]=True
        for i in range(1,n+1):
            dist[i]=min(dist[i],g[t][i])
    return res

def kruskal():
    edges.sort(key=lambda x:x[2])
    res,cnt=0,0
    for i in range(m):
        a,b,w=edges[i]
        a=find(a)
        b=find(b)
        if a!=b:
            p[a]=b
            res+=w
            cnt+=1
    
    
