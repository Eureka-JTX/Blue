#括号序列
MOD = (int)(1e9 + 7)
 
def add(x, y):  
    return (x + y) % MOD
 
def brackets():
    f = [[0 for i in range(n + 10)] for i in range(n + 10)]  
    f[0][0] = 1
 
    for i in range(1, n + 1):
        if str[i] == '(':
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j - 1]
        else:
            f[i][0] = add(f[i - 1][0], f[i - 1][1])
            for j in range(1, n + 1):
                f[i][j] = add(f[i - 1][j + 1], f[i][j - 1])
 
    for i in range(n + 1):
        if f[n][i]:
            return f[n][i]
 
str = list(input())
n = len(str)
 
str.insert(0, 0)  #使目标字符串下标从1开始
ans_l = brackets()
 
str.reverse()
for i in range(n):
    if str[i] == '(':
        str[i] = ')'
    else:
        str[i] = '('
str.insert(0, 0)  #使目标字符串下标从 1 开始
ans_r = brackets()
 
print(ans_l * ans_r % MOD)
 
