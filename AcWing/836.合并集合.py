N=100010
p=[x for x in range(N)]
n,m=map(int,input().split())

def find(x):
    if p[x]!=x: p[x]=find(p[x])
    return p[x]

for _ in range(m):
    op,a,b=input().split()
    if op=="M":
        p[find(int(a))]=find(int(b))  
    if op=="Q":
        if p[find(int(a))]==p[find(int(b))]: print("YES")
        else:   print("NO")
        
    
