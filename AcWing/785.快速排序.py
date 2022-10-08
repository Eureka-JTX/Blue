def quick_sort(a,l,r):
    if l>=r:    return
    x=a[(l+r)//2]
    i=l-1;
    j=r+1;
    while i<j:
        i+=1
        j-=1
        while a[i]<x:   i+=1
        while a[j]>x:   j-=1
        if i<j:     a[i],a[j]=a[j],a[i]
        
    quick_sort(a,l,j)
    quick_sort(a,j+1,r)
            
            
if __name__=='__main__':
    n=int(input())
    a=[int(x) for x in input().split()]
    quick_sort(a,0,n-1)
    print(' '.join(map(str,a)))


##选定分界点，小的放左大的放右，一轮后再分而治之
