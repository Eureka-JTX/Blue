N=100010
m=int(input())
stk,top=[0]*N,0     #定义栈和栈顶

def push(x):
    global top
    stk[top]=x
    top+=1

def pop():
    global top
    top-=1

def empty():
    global top 
    if top==0:
        print("YES") 
    else:
        print("NO")

def query():
    global top
    print(stk[top-1])

for _ in range(m):
    op, *p = input().split()
    if op == "push":
        push(int(p[0]))
    elif op == "query":
        query()
    elif op == "pop":
        pop()
    else:
        empty()
