##N=8
##path,used=[0]*N,[False]*N
##n=int(input())
##
##def dfs(u):
##    if u==n:
##        for i in range(n):
##            print(path[i],end=' ')
##        print()
##        return
##    for i in range(1,n+1):
##        if not used[i]:
##            path[u]=i
##            used[i]=True
##            dfs(u+1)
##            used[i]=False
##
##dfs(0)


##DFS+递归+回溯
##注意每次递归返回后要恢复现场，即将填写的数字恢复为未使用

N=10
path=[0]*N
n=int(input())

def dfs(num,state):
    if num>=n:
        for i in range(n):
            print(path[i],end=' ')
        print()
        return
    for i in range(n):
        if state>>i&1:  continue
        path[num]=i+1
        dfs(num+1,state|(1<<i))

dfs(0,0)

