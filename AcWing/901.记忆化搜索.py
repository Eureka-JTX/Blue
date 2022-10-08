N=310
directions=[(-1,0),(1,0),(0,-1),(0,1)]

def dp(x,y):
    if f[x][y]!=-1: return f[x][y]
    f[x][y]=1
    for d in directions:
        a,b=x+d[0],y+d[1]
        if a>=1 and a<=r and b>=1 and b<=c and w[x][y]>w[a][b]:
            f[x][y]=max(f[x][y],dp(a,b)+1)
    return f[x][y]

r,c=map(int,input().split())
f,w,res=[[-1]*N for _ in range(N)],[[0]],0
for i in range(1,r+1):
    w.append([0]+[int(x) for x in input().split()])
for i in range(1,r+1):
    for j in range(1,c+1):
        res=max(res,dp(i,j))
print(res)

##状态表示: f[i][j] 表示从 (i,j) 出发的点滑雪路径的最大和
##状态计算: 递归,判断 (i,j) 是否可以继续走下去
##f[i][j] = max(f[x][y], dp(x, y) + 1);
##初始化: f[i][j] = -1;如果能够走到那个点 f[x][y] = 1;
