n,m = map(int, input().split())
h = [0] + list(map(int, input().split()))

def down(k):
    global n
    u=k
    if 2*k<=n and h[u]>h[2*k]:    u=2*k
    if 2*k+1<=n and h[u]>h[2*k+1]:    u=2*k+1
    if u!=k:
        h[k],h[u]=h[u],h[k]
        down(u)
        
#初始化堆，找到最后一个非叶子节点
for i in range(n//2,0,-1):
    down(i)
    
#堆的重建
for _ in range(m):
    print(h[1],end=" ")
    h[1]=h[n]
    n-=1
    down(1)
    
