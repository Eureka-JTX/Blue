n,m=map(int,input().split())

##自己的写法：
##a=list(map(int,input().split()))
##for _ in range(m):
##    l,r=map(int,input().split())
##    s=0
##    while(l<=r):
##        s+=a[l-1]
##        l+=1
##    print(s)

##新建前缀和数组
##a=[0]+list(map(int,input().split()))
##s=[0]*(n+1)
##for i in range(1,n+1):
##    s[i]=s[i-1]+a[i]
##
##for _ in range(m):
##    l,r=map(int,input().split())
##    print(s[r]-s[l-1])


##直接把原数组改造为前缀和数组
a=[0]*(n+1)
a[1:n+1]=list(map(int,input().split()))

for i in range(1,n+1):
    a[i]+=a[i-1]

for i in range(m):
    l,r=map(int,input().split())
    print(a[r]-a[l-1])
