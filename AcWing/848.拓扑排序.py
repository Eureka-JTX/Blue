##有向图的拓扑排序的基本思想是：首先在有向图中选取一个没有前驱的顶点，将其输出，
##从有向图中删除该顶点，并且删除以该顶点为尾的所有有向图的边。
##重复以上的步骤，直到图中的所有顶点均输出或是图中的顶点均没有前驱为止。
##对于后者，说明有向图中存在环，不能进行拓扑排序。
from collections import deque
N=100010
h,e,ne,idx=[-1]*N,[0]*N,[0]*N,0
q,d,ans=deque(),[0]*N,[]

def insert(a,b):
    global idx
    e[idx]=b
    ne[idx]=h[a]
    h[a]=idx
    idx+=1

def topsort():
    for i in range(1,n+1):
        if d[i]==0:     q.append(i)
    while q:
        tmp=q.popleft()
        ans.append(tmp)
        i=h[tmp]
        while i!=-1:
            j=e[i]
            d[j]-=1
            if d[j]==0:     q.append(j)
            i=ne[i]
    return len(ans)==n

n,m=map(int,input().split())
for _ in range(m):
    a,b=map(int,input().split())
    insert(a,b)
    d[b]+=1
if topsort():   print(" ".join(map(str,ans)))
else:   print("-1")

            
    
    
