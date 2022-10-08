n=int(input())
a=list(map(int,input().split()))
target=int(input())

def bisect(target):
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]<ta rget:
            l=mid+1
        elif a[mid]>target:
            r=mid-1
        else:
            return mid
    return -1

def bisect_left(target):
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]<target:
            l=mid+1
        elif a[mid]>=target:
            r=mid-1
    if l>=n or a[l]!=target:
        return -1
    return l

def bisect_right(target):
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]<=target:
            l=mid+1
        elif a[mid]>target:
            r=mid-1
    if r<0 or a[r]!=target:
        return -1
    return r
    
print(bisect(target))
print(bisect_left(target))
print(bisect_right(target))
