n,m,q=map(int,input().split())

##构造n+1行，m+1列数组（第一行第一列全为0）
a=[[0]*(m+1) for _ in range(n+1)]

##注意二维数组的初始化
for i in range(1,n+1):
    a[i][1:]=list(map(int,input().split()))

##直接把原数组改造为前缀和数组，节省空间
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i][j]+=a[i-1][j]+a[i][j-1]-a[i-1][j-1]
for _ in range(q):
    x1,y1,x2,y2=map(int,input().split())
    ans=a[x2][y2]-a[x2][y1-1]-a[x1-1][y2]+a[x1-1][y1-1]
    print(ans)
