n=int(input())
a=[int(x) for x in input().split()]
a.sort()

res=0
for i in range(n):
    res+=a[i]*(n-i-1)
print(res)
