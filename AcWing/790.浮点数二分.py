n=float(input())
l,r=-10000,10000

while r-l>1e-8:
    mid=(l+r)/2
    if mid**3>=n:
        r=mid
    else:
        l=mid
print("{:.6f}".format(l))
