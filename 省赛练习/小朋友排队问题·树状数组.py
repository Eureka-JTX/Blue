#   树状数组解法
n=int(input())
N=1000010
#注意树状数组下标应从1开始，而小朋友身高有可能为0，所以在输入时身高全加1，不影响逆序对
h=[-1]+[int(i)+1 for i in input().split()]  
c=[0]*N    #树状数组
cnt=[0]*N       #记录每个小朋友的交换次数
m=max(h)
def lowbit(n):
    return n&(-n)

def update(x):
    i=x
    while i<=m:
        c[i]+=1
        i+=lowbit(i)

def getsum(x):
    sum,i=0,x
    while i>=1:
        sum+=c[i]
        i-=lowbit(i)
    return sum

#求左边比他大的数
for i in range(1,n+1):
    update(h[i])
    cnt[i]+=i-getsum(h[i])

#求右边比他小的数
c=[0]*N
for i in range(n,0,-1):
    update(h[i])
    cnt[i]+=getsum(h[i]-1)

ans=0
for i in range(1,n+1):
    ans+=cnt[i]*(cnt[i]+1)//2
print(ans)
