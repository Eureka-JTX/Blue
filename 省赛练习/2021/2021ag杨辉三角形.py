def C(a,b):
    res=1
    for i in range(a):
        res*=b/a
        if res>target:
            break
        b-=1
        a-=1
    return res

def search(k):
    low=2*k
    high=target
    if high<=low and C(k,low)!=target:
        return False
    while low<=high:
        mid=low+(high-low)//2
        if C(k,mid)<target:
            low=mid+1
        elif C(k,mid)>target:
            high=mid-1
        else:
            print(int((mid+1)*mid/2)+k+1)
            return True
    return False

target=int(input())
for i in range(16,-1,-1):
    if search(i):
        break
