m=int(input())
N=100010
e,l,r,idx = [0]*N,[0]*N,[0]*N,0

def init():
    global idx
    r[0],l[1],idx=1,0,2
#约定左端点为0，右端点1，插入时index从第2个开始算
#实际上插入时k从1开始算，因此index=k+1
    
def remove(k):
    l[r[k]]=l[k]
    r[l[k]]=r[k]
    
#在第 k 个插入的数右侧插入一个数；
def insert(k,x):
    global idx
    e[idx],l[idx],r[idx],l[r[k]],r[k],idx=x,k,r[k],idx,idx,idx+1

init()    
for _ in range(m):
    op,*p=input().split()
    if op=="L":
        x=int(p[0])
        insert(0,x)
    elif op=="R":
        x=int(p[0])
        insert(l[1],x)
    elif op=="D":
        k=int(p[0])
        remove(k+1)
    elif op=="IL":
        k,x=map(int,p)
        insert(l[k+1],x)
    elif op=="IR":
        k,x=map(int,p)
        insert(k+1,x)

i = r[0]
while i!=1:     #不等于右端点
    print(e[i], end=" ")
    i=r[i]

    
    
