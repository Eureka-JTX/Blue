def bfs(x,y):
  d=[(-1,0),(1,0),(0,1),(0,-1)]
  q=[(i,j)]
  vis[i][j]=1
  global flag
  while q:
    t=q.pop(0)
    tx,ty=t[0],t[1]
    if mp[tx][ty-1]==mp[tx][ty+1]==mp[tx-1][ty]==mp[tx+1][ty]=='#':
      flag=1
    for n in range(4):
      nx,ny=tx+d[n][0],ty+d[n][1]
      if vis[nx][ny]==0 and mp[nx][ny]=='#':
        q.append((nx,ny))
        vis[nx][ny]=1
        
n=int(input())
mp=[]
ans=0
for _ in range(n):
  mp.append(list(input()))
vis=[[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if vis[i][j]==0 and mp[i][j]=='#':
      flag=0
      bfs(i,j)
      if flag==0:
        ans+=1
print(ans)
