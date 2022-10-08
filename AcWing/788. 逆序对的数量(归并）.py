def merge_sort(a,l,r):
    if l>=r:
        return 0
    
    mid=(l+r)//2
    tmp,i,j=[],l,mid+1
    res=merge_sort(a,l,mid)+merge_sort(a,mid+1,r)

    while i<=mid and j<=r:
        if a[i]<=a[j]:
            tmp.append(a[i])
            i+=1
        else:
            tmp.append(a[j])
            j+=1
            res+=mid-i+1

    if i<=mid:
        tmp.extend(a[i:mid+1])
    if j<=r:
        tmp.extend(a[j:r+1])
    a[l:r+1]=tmp[:]

    return res

n=int(input())
a=[int(x) for x in input().split()]
print(merge_sort(a,0,n-1))

##分析左右两半部分，如果左半部分 q[i] 大于右半部分的 q[j]，
##那么从 i 到 mid 都可以和 j 组成逆序对，
##逆序对个数 res += mid - i + 1

##https://www.bilibili.com/video/BV1Qk4y1r7u5?from=search&seid=9548284191279485650&spm_id_from=333.337.0.0
