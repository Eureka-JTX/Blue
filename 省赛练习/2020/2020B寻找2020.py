def hang():
    global cnt
    if j+3<n and s[i][j+1]==s[i][j+3]=='0' and s[i][j+2]=='2':  cnt+=1

def lie():
    global cnt
    if i+3<m and s[i+1][j]==s[i+3][j]=='0' and s[i+2][j]=='2':  cnt+=1

def xie():
    global cnt
    if j+3<n and i+3<m and s[i+1][j+1]==s[i+3][j+3]=='0' and s[i+2][j+2]=='2':  cnt+=1
            
f=open("1.txt","r")
s=f.read().split("\n")
m,n=len(s),len(s[0])
cnt=0
for i in range(m):
    for j in range(n):
        if s[i][j]=='2':
            hang()
            lie()
            xie()
print(cnt)
            
