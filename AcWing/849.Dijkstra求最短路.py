N,null=510,0x3f3f3f3f
g=[[null]*N for _ in range(N)]
# dist 用于存储每个点到起点的最短距离
# st 用于在更新最短距离时 判断当前点的最短距离是否确定 是否需要更新
dist,st=[null]*N,[False]*N

def dijkstra():
    dist[1]=0
# 第一个for循环是找出没有被确认的最短路径的点集合中离源点最近的点
# 第二个for循环是用选出的这个点来更新源点到其他点的最短路径（只用更新
# 没被确认的相邻的点，但是为了代码方便就直接全部更新）
    for _ in range(n):
        t=-1
        for i in range(1,n+1):
            if not st[i] and (t==-1 or dist[t]>dist[i]):
                t=i
        st[t]=True
        for i in range(1,n+1):
            dist[i]=min(dist[t]+g[t][i],dist[i])    
    if dist[n]==null:   return -1
    else:   return dist[n]
    
n,m=map(int,input().split())
for _ in range(m):
    x,y,z=map(int,input().split())
    g[x][y]=min(g[x][y],z)
print(dijkstra())





