###拉链法    
##N=100001
##def prime(x):
##    for i in range(2,x//2):
##        if x%i==0:
##            return False
##    return True
##while not prime(N):
##    N+=1
##
##n=int(input())
##h,e,ne,idx=[-1]*N,[0]*N,[0]*N,0
####h 数组下标是 x 哈希之后的值，存储的值相应 idx
####e[idx] 表示 h 引出单链表下标为 idx 的值
####ne[idx] 存储下标为 idx 的下一个位置的下标
####idx 单链表的下标
##
##def insert(x):
##    global idx
##    k=x%N
##    e[idx]=x
##    #从头插入
##    ne[idx]=h[k]
##    h[k]=idx
##    idx+=1
##
##def query(x):
##    global idx
##    k=x%N
##    index=h[k]
##    while index!=-1:
##        if e[index]==x:
##            print("YES")
##            return
##        index=ne[index]
##    print("NO")

#开放寻址法
#N为初始化 2~3 倍空间的第一个质数
N, null = 200003, 0x3f3f3f3f
h = [null]*N

def find(x):
    k=x%N
    while h[k]!=null and h[k]!=x:
        k+=1    #如果坑被占就往后走1
        if k==N:    k=0
    return k

n=int(input())

for _ in range(n):
    op, px = input().split()
    px = int(px)
    k=find(px)
    if op == "I":
        h[k]=px
    elif op=="Q":
        if h[k]==null:  print("NO")
        else:   print("YES")
