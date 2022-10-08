n,k=map(int,input().split())
a=[]
for i in range(k):
  a.append(int(input()))
a.sort()

def check(Q):
    L=0                 #初始左边界
    for i in range(k):
        if L+Q>=a[i]:   #即能扫描到第i个机器人
            if L>=a[i]:  #上个机器人能清扫到这个机器人，那么机器人只需要考虑往右扫描就够了
                L=a[i]+Q-1
            else:       #上个机器人不能扫到这个机器人，要保证能扫到左边界，再往右扫描
                L=L+Q
        else:
            return False
    return L>=n

def binary():
#这道题实际上就是让我们搜索每个机器人负责清扫的范围
    l,r=0,n-1
    ans=1
    while l<=r:
        mid=(l+r)//2
        if check(mid):  #能扫描完全部
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(2*(ans-1))

binary()

            
