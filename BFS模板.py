from collections import deque
def bfs(x,y):
    move=[(-1,0),(1,0),(0,1),(0,-1)]
    q=deque()
    q.qppend((x,y))
    for i in range(n):
        t=q.popleft()
        r,c=t[0],t[1]
        for _ in range(4):
            nr,nc=r+move[0],c+move[1]
            if inarea(nr,nc) and g[nr][nc]==0:
                g[nr][nc]=2
                q.append((nr,nc))
    
