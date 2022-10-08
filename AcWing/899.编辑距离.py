# acwing 899. 编辑距离
 
def edit_distance(a,b):
    len_a, len_b = len(a)-1, len(b)-1
    f = [[0]*(len_b+1) for _ in range(len_a+1)]
 
    for i in range(1,len_a+1):
        f[i][0] = i
    for i in range(1,len_b+1):
        f[0][i] = i
 
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            # 最后一步变或者不变，变有三种方式
            if a[i] == b[j]: f[i][j] = f[i-1][j-1]
            else: f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1]) + 1
    return f[len_a][len_b]
 
 
if __name__ == '__main__':
    a = []
    n, m = map(int, input().split())
    for _ in range(n):
        a.append(' ' + input())
    for _ in range(m):
        inp_list = input().split()
        res, s, t = 0, ' ' + inp_list[0], int(inp_list[1])
        for j in range(n):
            if edit_distance(a[j],s) <= t: res += 1
        print(res)
 
 
 
N = 1010
 
def edit_distance(a1,b1):
    n1, m1 = len(a1)-1, len(b1)-1
    f = [[0]*(m1+1) for _ in range(n1+1)]
 
    for i in range(n1+1):
        f[i][0] = i
    for i in range(m1+1):
        f[0][i] = i
 
    for i in range(1,n1+1):
        for j in range(1,m1+1):
            f[i][j] = min(f[i][j-1]+1, f[i-1][j]+1, f[i-1][j-1] + int(a1[i]!=b1[j]))
    return f[n1][m1]
 
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(' ' + input())
    for i in range(m):
        in_li = input().split()
        res, s, t = 0, ' ' + in_li[0], int(in_li[1])
        for j in range(n):
            if edit_distance(a[j],s) <= t: res+=1
        print(res)
 
