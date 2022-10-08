def func(x,y):
    x1,y1=x,y
    while y1:
        x1,y1=y1,x1%y1
    return x*y//x1

dp=[float("inf")]*2022
dp[1]=0
for i in range(1,2022):
    for j in range(i+1,i+22):
        if j>2021:
            break
        dp[j]=min(dp[j],dp[i]+func(j,i))
print(dp[2021])
