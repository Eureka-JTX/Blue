N=1010
n=int(input())
a=[int(x) for x in input().split()]

#普通DP
##f=[1]*N
##for i in range(n):
##    for j in range(i):
##        if a[j]<a[i]:
##            f[i]=max(f[i],f[j]+1)
##print(max(f))

#二分优化
def b_serach():
    l,r=-1,len+1
    while l+1!=r:
        mid=(l+r)//2
        if f[mid]<=a[i]:    l=mid
        else:   r=mid
    return r
    
f,len=[a[0]]+[0]*N,0
for i in range(n):
    if a[i]>f[len]:
        len+=1
        f[len]=a[i]
    else:
        f[b_serach()]=a[i]  #在f中找出第一个大于a[i]的数并交换
print(len+1)
