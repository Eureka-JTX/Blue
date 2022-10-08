N=100010
m=int(input())
q,h,t=[0]*N,0,-1     #定义队列、队头队尾

def push(x):
    global t
    t+=1
    q[t]=x

def pop():
    global h
    h+=1

def empty():
    global h,t 
    if h==t+1:
        print("YES") 
    else:
        print("NO")

def query():
    global q,h
    print(q[h])

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
