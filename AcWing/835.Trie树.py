##https://www.bilibili.com/video/BV1Az4y1S7c7?from=search&seid=8782717501553818513&spm_id_from=333.337.0.0
##高效存储和查找字符串
##0号点既是根节点，又是空节点
##son[][]存储树中每个节点的子节点
##cnt[]存储以每个节点结尾的单词数量
##idx 结点的下标
N=100010
son=[[0]*26 for _ in range(N)]
cnt=[0]*N
idx=0

def insert(s):
    global son,cnt,idx
    p=0
    for i in range(len(s)):
        j=ord(s[i])-ord('a')
        if not son[p][j]:
            idx+=1
            son[p][j]=idx
        p=son[p][j]
    cnt[p]+=1

def query(s):
    global son,cnt,idx
    p=0
    for i in range(len(s)):
        j=ord(s[i])-ord("a")
        if not son[p][j]:   return 0
        p=son[p][j]
    return cnt[p]

n=int(input())
for _ in range(n):
    p,s=input().split()
    if p=="I":
        insert(s)
    if p=="Q":
        print(query(s))
