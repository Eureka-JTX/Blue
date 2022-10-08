n,m=map(int,input().split())
a,b=[0]*(n+2),[0]*(n+2)
a[1:n+1]=list(map(int,input().split()))

def insert(l,r,c):
    b[l]+=c
    b[r+1]-=c
    
for i in range(1,n+1):
    insert(i,i,a[i])

for i in range(m):
    l,r,c=map(int,input().split())
    insert(l,r,c)

for i in range(1,n+1):
    b[i]+=b[i-1]
    print(b[i],end=' ')


##差分相当于前缀和的逆操作，通过对差分数组进行前缀和操作就可以还原原数组
##让数组a某段（l,r）每个元素都加上（连续加多次）某一值的操作从O(n)->O(1)，
##    只需要将b[l]+c,b[r+1]-c
##为什么可以把初始化也当成更新操作，首先你假设a数组全为0，则差分数组b也全为0。
##    现在你要做的更新操作就是在数组a[1,1]，[2,2]，[3,3]...的范围依加上a1,a2,a3...，
##    则相当于在数组b[1]+a1,b[2]-a1、b[2]+a2,b[3]-a2
    
