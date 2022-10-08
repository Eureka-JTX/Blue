N = 100010
n = int(input())
##h[N]存储堆中的值, h[1]是堆顶，x的左儿子是2x, 右儿子是2x + 1
##ph[index]存储第index个插入的点在堆中的位置
##hp[size]存储堆中下标是size的点是第几个插入的
h, hp, ph, size, index = [0]*N, [0]*N, [0]*N, 0, 0

#堆构造、重建
def down(k):
    global size
    u = k
    if 2*k<=size and h[u]>h[2*k]: u=2*k
    if 2*k+1<=size and h[u]>h[2*k+1]: u=2*k+1
    if u!=k:
        heap_swap(k,u)
        down(u)

#更新节点位置
def up(k):
    global size
    while k//2 and h[k//2]>h[k]:
        heap_swap(k//2,k)
        k//=2

def heap_swap(i,j):
    # 原本堆中第i个位置是第hp[i]次插入的，
    # 由于改变了堆中的顺序，现在第hp[i]次插入的是j
    # 原本这个位置记录的插入堆的位置是i，现在要改为j
    ph[hp[i]], ph[hp[j]] = j, i
    hp[i],hp[j] = hp[j],hp[i]
    h[i],h[j]=h[j],h[i]

for _ in range(n):
    op, *px = input().split()
    if op == "I":
        x = int(px[0])
        size+=1
        index+=1
        ph[index],hp[size]=size,index
        h[size]=x
        up(size)
    elif op == "PM":
        print(h[1])
    elif op == "DM":
        heap_swap(1,size)
        size-=1
        down(1)
    elif op == "D":
        k = int(px[0])
        k=ph[k]
        heap_swap(k,size)
        size-=1
        down(k)
        up(k)
    elif op=="C":
        k, x = map(int, px)
        k=ph[k]
        h[k]=x
        down(k)
        up(k)
