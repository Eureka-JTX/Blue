def dfs(num,state):
    if num>=n:
        for i in range(n):
            if state>>i&1:
                print(i+1,end=' ')  #1就是选了该数字
        print()
        return
    dfs(num+1,state)    #不选择num+1
    dfs(num+1,state|(1<<num))   #选

n=int(input())
dfs(0,0)
        
