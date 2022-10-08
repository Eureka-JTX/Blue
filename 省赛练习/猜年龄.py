from itertools import permutations as per
for p in per("1234567890"):
  a=int(''.join(p[:4]))
  b=int(''.join(p[4:]))
  for i in range(50):
      if pow(i,3)==a:
        if pow(i,4)==b:
            print(i)
            break
