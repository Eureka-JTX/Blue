def merge_sort(a,l,r):
    if l>=r:
        return
    
    mid=(l+r)//2
    merge_sort(a,l,mid)
    merge_sort(a,mid+1,r)
    
    tmp,i,j=[],l,mid+1
    while i<=mid and j<=r:
        if a[i]<a[j]:
            tmp.append(a[i])
            i+=1
        else:
            tmp.append(a[j])
            j+=1
    if i<=mid:
        tmp+=a[i:mid+1]
    if j<=r:
        tmp+=a[j:r+1]
    a[l:r+1]=tmp[:]
    
if __name__=="__main__":
    n=int(input())
    a=[int(x) for x in input().split()]
    merge_sort(a,0,n-1)
    print(" ".join(map(str,a)))

##  归并排序特点是先分后治，比较两组最左端找最小的数合成新的组，
##                          保证每次合成的新组有序
