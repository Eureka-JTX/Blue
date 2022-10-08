def inarea(x,y):
    return 0<=x<m and 0<=y<n

def dfs(x,y):
    if not inarea(x,y): return
    if g[x][y]!=1:  return

    g[x][y]=2
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

for i in range(m):
    for j in range(n):
        if g[i][j]==1:
            dfs(i,j)
