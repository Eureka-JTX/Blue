c=[0]*n

def lowbit(n):
    return n&(-n)

def update(x):
    i=x
    while i<=m:
        c[i]+=1
        i+=lowbit(i)

def getsum(x):
    sum,i=0,x
    while i>=1:
        sum+=c[i]
        i-=lowbit(i)
    return sum
