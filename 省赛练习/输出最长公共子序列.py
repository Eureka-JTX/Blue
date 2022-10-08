def lcs(s1,s2):
    len1=len(s1)
    len2=len(s2)
    res=[[0]*(len1+1) for i in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if s2[i-1]==s1[j-1]:
                res[i][j]=res[i-1][j-1]+1
            else:
                res[i][j]=max(res[i-1][j],res[i][j-1])
    s=""
    i,j=len2,len1
    while i>0 and j>0:
        if s2[i-1]==s1[j-1]:
            s=s+s2[i-1]
            i-=1
            j-=1
        else:
            if res[i-1][j]>res[i][j-1]: #换为>= 是另一种子序列
                i-=1
            else:
                j-=1
    return res[-1][-1],s[::-1]

print(lcs("123456778","357486782"))
