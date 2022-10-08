n=int(input())
a=list(map(int,input().split()))
b=[0]*100001
j,ans=0,0
for i in range(n):
    b[a[i]]+=1
    while b[a[i]]>1:
        b[a[j]]-=1
        j+=1
    ans=max(ans,i-j+1)
print(ans)

##https://blog.csdn.net/weixin_41126303/article/details/120734788
