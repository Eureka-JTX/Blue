def lcs(s1,s2):
    len1=len(s1)
    len2=len(s2)
    res=[[0]*(len1+1) for i in range(len2+1)]
    mlen=0
    index=0
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if s2[i-1]==s1[j-1]:
                res[i][j]=res[i-1][j-1]+1
                if mlen<res[i][j]:
                    mlen=res[i][j]
                    index=i
    s=s2[index-mlen:index]  #从第i-1-len+1输出到第i-1
    return mlen,s

print(lcs("123456778","357486782"))
