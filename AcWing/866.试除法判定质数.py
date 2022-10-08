def is_prime(x):
    if x<2: return False
    for i in range(2,x):
        if i>x/i:   return True
        if x%i==0:  return False

n=int(input())
for _ in range(n):
    m=int(input())
    print(is_prime(m))



    
