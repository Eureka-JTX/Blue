b=[]
l=[0]*5
dp=[0]*305
for i in range(6):
    a=list(map(int,input().split()))
    for j in range(1,len(a)):
        l[a[j]]+=1
n=sum(l)
m=int(input())
for i in range(m):
    b.append(list(map(int,input().split())))
b=sorted(b,key=lambda x:x[0])

sum=0
kind=0
for level in range(4,0,-1):
    sum+=l[level]
    if sum==0:
        continue
    for i in range(m):
        if b[i][0]==level:
            for k in range(sum,-1,-1):
                for j in range(1,b[i][1]+1):
                    if k>=j:
                        dp[k]=max(dp[k],dp[k-j]+b[i][j+1])
ans=0
for i in range(sum+1):
    ans=max(ans,dp[i])
print(ans)
            
                
        
    
