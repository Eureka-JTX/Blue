n=int(input())
w=[int(x) for x in input().split()]
w.sort()

res=0
for i in range(n):
    res+=abs(w[n//2]-w[i])
print(res)
