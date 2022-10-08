from collections import deque
maze=[]
m,n=map(int,input().split())
for _ in range(m):
    maze.append(list(input()))
q=deque()
q.append((0,0,''))
v=[[False]*n for _ in range(m)]
while q:
    x,y,path=q.popleft()
    if x==m-1 and y==n-1:
        print(path)
        break
    for (dx,dy,dz) in enumerate([(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]):
        x1,y1=dx+x,dy+y
        if 0<=x1<m and 0<=y1<n and maze[x1][y1]=='0' and not v[x1][y1]:
            q.append((x1,y1,path+dz))
            v[x1][y1]=True
            
        
    

