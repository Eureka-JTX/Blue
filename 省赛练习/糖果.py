n,m,k=map(int,input().split())
dp=[0x3f3f3f3f]*(1<<m)
a=[0]*(n+1)
c=[0]*m
flag=False

for i in range(1,n+1):
    t=[0]+list(map(int,input().split()))
    for i in range(1,k+1):
        t[i]-=1
        a[i]|=(1<<t[i])
        c[t[i]]+=1

for i in range(m):
    if c[i]==0:
        flag=True
        print(-1)
        break

if not flag:
    dp[0]=0
    for i in range(1,n+1):
        for j in range((1<<m)-1,-1,-1):
            dp[j|a[i]]=min(dp[j|a[i]],dp[j]+1)
    print(dp[(1<<m)-1])


        
    

        
    
    





