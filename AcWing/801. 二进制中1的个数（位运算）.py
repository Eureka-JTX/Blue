##1. 求 n 的第 k 位数字： n >> k & 1
##2. 返回 x 的最后一位 1：lowbit(x)
##原理：x & -x;x & -x 其实就是 x & (~x + 1)
##3. 补码是原码取反再加一

n=int(input())
a=list(map(int,input().split()))

def lowbit(x):
    return x&(-x)

for i in range(n):
    res=0
    while a[i]:
        a[i]-=lowbit(a[i])
        res+=1
    print(res,end=" ")

