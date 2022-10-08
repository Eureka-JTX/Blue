from itertools import permutations as per
def calc(l,r):
    res=0
    for i in range(l,r+1):
        res=10*res+int(p[i])
    return res
for p in per("0123456789"):
    if int(p[0]) and int(p[4]) and int(p[8]):
        a,b,c=calc(0,3),calc(4,7),calc(8,9)
        if (a-b)*c==900:
            print(a,b,c)

    
    
