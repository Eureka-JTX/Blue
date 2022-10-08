##专指整数、有序，用于值域很大，个数很少
##数据范围为 10 的 9 次方,如果直接一个数组来存,空间就会超出限制
##但是操作数和查询数只有 10 的 5 次方
##想到用离散化的方式,用 10 的 5 次方的长度表示 10 的 9 次方的量级
##申请的数组长度 n + m + m + 10 就可以,加个 10 防止边界问题
    
n,m=map(int,input().split())
a,s=[0]*300010,[0]*300010
alls,add,query=[],[],[]
for _ in range(n):
    x,c=map(int,input().split())
    add.append((x,c))
    alls.append(x)
for _ in range(m):
    l,r=map(int,input().split())
    query.append((l,r))
    alls.append(l)
    alls.append(r)

##集合化alls，去重排序
alls=list(set(alls))
alls.sort()

##用二分求出x离散化的值,找到第一个大于x的数
def find(x):
    l,r=-1,len(alls)
    while l+1!=r:
        mid=(l+r)//2
        if alls[mid]<=x:
            l=mid
        else:
            r=mid
    return r

for x,c in add:
    a[find(x)]+=c

for i in range(1,300010):
    s[i]=s[i-1]+a[i]

for l,r in query:
    print(s[find(r)]-s[find(l)-1])
          
