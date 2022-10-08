# n = int(input())
# s = set()
# for i in range(2, n + 1):
#     if n < i:
#         break
#     while n % i == 0:
#         s.add(i)
#         n //= i
# if n != 1:
#     s.add(n)
#
# print(len(s))

n = int(input())
i = 2
ans = 0
while i * i <= n:
    if n % i == 0:
        ans += 1
        while n % i == 0:
            n //= i
    i += 1
if n > 1:
    ans += 1
print(ans)
