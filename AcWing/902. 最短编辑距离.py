N = 1010
n, a = int(input()), ' ' + input()
m, b = int(input()), ' ' + input()
f = [[0]*N for _ in range(N)]
for i in range(1,n+1):
    f[i][0]=f[0][i]=i
for i in range(1,n+1):
    for j in range(1,m+1):
        f[i][j]=min(f[i-1][j],f[i][j-1])+1
        f[i][j]=min(f[i][j],f[i-1][j-1]+int(a[i]!=b[j]))
print(f[n][m])
