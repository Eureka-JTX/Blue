N=10e9+7
def dfs(x,y,num,max):
  if dp[x][y][num][max+1]!=-1:
    return dp[x][y][num][max+1]   #记忆化搜索 
  if x==n and y==m:
    if num==k or (num==k-1 and max<mp[x][y]):
      dp[x][y][num][max+1]=1
    else:
      dp[x][y][num][max+1]=0
    return  dp[x][y][num][max+1]
  s=0
  if x+1<=n:
    if max<mp[x][y]:
      s+=dfs(x+1,y,num+1,mp[x][y])
    s+=dfs(x+1,y,num,max)
  if y+1<=m:
    if max<mp[x][y]:
      s+=dfs(x,y+1,num+1,mp[x][y])
    s+=dfs(x,y+1,num,max)
  dp[x][y][num][max+1]=s%N
  return  dp[x][y][num][max+1]
    
n,m,k=map(int,input().split())
mp=[[0]*(m+1)]
for i in range(n):
  mp.append([0]+list(map(int,input().split())))
dp=[[[[-1]*55 for _ in range(55)] for _ in range(15)] for _ in range(15)]
print(mp)
print(int(dfs(1,1,0,-1)))
