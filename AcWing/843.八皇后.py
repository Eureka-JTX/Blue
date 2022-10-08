N=20
T=0

def dfs(u):
    if u==n:
        global T
        T=T+1
        print('第',T,'种摆法：')
        for i in range(n):
            print(''.join(path[i]))
        print()
        return
    for i in range(n):
        if col[i] and dg[n+u-i] and ndg[u+i]:
            path[u][i]='Q'
            col[i],dg[n+u-i],ndg[u+i]=False,False,False
            dfs(u+1)
            path[u][i]='.'
            col[i],dg[n+u-i],ndg[u+i]=True,True,True

if __name__=='__main__':
    n=int(input())
    dg,ndg,col=[True]*N, [True]*N,[True]*N
    path=[['.']*n for _ in range(n)]

    dfs(0)
    
##类似842.全排列，区别是引入二维数组
##注意：       u是行，i是列
##python中关于二维数组的初始化
##在函数中使用全局变量需要声明
##打印列表想不带括号用join
