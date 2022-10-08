def dfs(num,state,start):
    if num>=m:
        for i in range(m):
            print(a[i],end=' ')
        print()
        return
    for i in range(start,n):
        a[num]=i+1
        dfs(num+1,state|(1<<i),i+1)
