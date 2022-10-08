N,P,Q=100010,131,91815541
# h[k]数组是字符串前k个字母的hash值
# p[k]存储 P^k mod q
h,p=[0]*N,[0]*N
n,m=map(int,input().split())
p[0]=1
s=" "+input()
for i in range(1,n+1):
    p[i]=p[i-1]*P%Q
    h[i]=(h[i-1]*P+ord(s[i]))%Q

def get(l,r):
    return (h[r]-h[l-1]*p[r-l+1])%Q
#前缀和、空间和

for _ in range(m):
    l1,r1,l2,r2=map(int,input().split())
    if get(l1,r1)==get(l2,r2):  print("YES")
    else:   print("NO")

