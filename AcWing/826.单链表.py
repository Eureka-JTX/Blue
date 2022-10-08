m=int(input())
N=100010
# head表示头节点下表，e[i]表示节点i的值
# ne[i]表示节点i的next指针是多少，idx表示存储当前已经用到了哪个点
e,ne,idx,head = [0]*N,[0]*N,1,0

def insert_to_head(x):
    global idx,head
    e[idx],ne[idx],head,idx=x,head,idx,idx+1

def remove(k):
    global idx
    ne[k]=ne[ne[k]]

def insert(k,x):
    global idx
    e[idx],ne[idx],ne[k],idx=x,ne[k],idx,idx+1
    
for _ in range(m):
    op,*p=input().split()
    if op=="H":
        x=int(p[0])
        insert_to_head(x)
    if op=="D":
        k=int(p[0])
        if k==0:
            head=ne[head]
        else:
            remove(k)
    if op=="I":
        k,x=map(int,p)
        insert(k,x)

while head!=0:
    print(e[head],end=" ")
    head=ne[head]

    
    
