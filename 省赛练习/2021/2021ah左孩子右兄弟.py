import sys
sys.setrecursionlimit(10**5)

def dfs(u):
    ans=0
    cnt=len(child[u])
    for i in range(0,cnt):
        ans=max(ans,dfs(child[u][i])+cnt)
    return ans

n=int(input())
child=[[] for i in range(10**5+10)]
for i in range(2,n+1):
    tmp=int(input())
    child[tmp].append(i)
print(dfs(1))

    
