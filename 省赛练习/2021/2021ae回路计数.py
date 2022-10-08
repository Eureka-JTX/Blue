from math import gcd
dp=[[0 for j in range(21)] for i in range(2**21)]
#dp[i][j]代表在j点已走过状态为i方案数
dp[1][0]=1
road=[[False]*21 for i in range(21)]
for i in range(21):
    for j in range(21):
        if gcd(i+1,j+1)==1:
            road[i][j]=True
for i in range(1,2**21):
    for j in range(21):
        if i>>j&1:
            for k in range(21):
                if i-2**j>>k&1 and road[k][j]:
                    dp[i][j]+=dp[i-2**j][k]
print(sum(dp[2**21-1])-dp[2**21-1][0])
    
