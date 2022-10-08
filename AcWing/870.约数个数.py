from collections import defaultdict

M=int(1e9+7)
def get_prime(x):
    for i in range(2,x+1):
        if i>x/i:   break
        while x%i==0:
            x//=i
            primes[i]+=1
    if x>1: primes[x]+=1
        
n,primes,ans=int(input()),defaultdict(int),1
for _ in range(n):
    get_prime(int(input()))
for p in primes.values():
    ans*=(p+1)
print(ans%M)
