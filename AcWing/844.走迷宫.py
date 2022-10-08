from collections import deque
directions=[(-1,0,'U'),(0,-1,'L'),(0,1,'R'),(1,0,'D')]

def bfs():
    ans=[]
    while q:
        tmp=q.popleft()
        for direction in directions:
            x,y=tmp[0]+direction[0],tmp[1]+direction[1]
            if x>=0 and x<n and y>=0 and y<m and g[x][y]=='0' and d[x][y]==-1:
                d[x][y]=d[tmp[0]][tmp[1]]+1
                q.append((x,y))
                ans.append(direction[2])
    print(''.join(map(str,ans)))

n,m=map(int,input().split())
g,d,q=[],[[-1]*m for _ in range(n)],deque()
for i in range(n):
    g.append(list(input()))
d[0][0]=0
q.append((0,0))
bfs()

#g是迷宫图，0——1矩阵    d存储该点到0,0点的距离，负1代表未访问过    q是队列

