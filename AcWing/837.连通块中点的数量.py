n,m=map(int,input().split())
p=[x for x in range(n+1)]
size=[1]*(n+1)

def find(x):
    if p[x]!=x: p[x]=find(p[x])
    return p[x]
for _ in range(m):
    op,*s=input().split()
    if op=="C":
        a,b=int(s[0]),int(s[1])
        if a!=b:
            size[find(b)]+=size[find(a)]
            p[find(a)]=find(b)
    if op=="Q1":
        a,b=int(s[0]),int(s[1])
        if a==b:    print("YES")
        else:
            if find(a)==find(b): print("YES")
            else:   print("NO")
    if op=="Q2":
        a=int(s[0])
        print(size[find(a)])
