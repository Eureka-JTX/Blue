N=100010

def find(x):
    if p[x]!=x:     p[x]=find(p[x])
    return p[x]

def kruskal():
    edges.sort(key=lambda x:x[2])
    res,cnt=0,0
    for i in range(m):
        a,b,w=edges[i]
        a,b=find(a),find(b)
        if a!=b:
            p[a]=b
            res+=w
            cnt+=1
    if cnt<(n-1):   return 'impossible'
    else:   return res
    
p,edges=[x for x in range(N)],[]
n,m=map(int,input().split())
for _ in range(m):
    u,v,w=map(int,input().split())
    edges.append((u,v,w))
print(kruskal())
   
