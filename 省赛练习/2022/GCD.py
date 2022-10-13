# # gcd(a+k,b+k)=gcd(b-a,a+k)
# # (a+k)%i==0,(a%i+k%i)==(1||0),=>   k=(i-a%i)%i
# from math import gcd, sqrt
#
# fac = []
# t = int(input())
# for _ in range(t):
#     ans = -0x3f3f3f3f
#     ansk = 1
#     a, b = map(int, input().split())
#     t = b - a
#     for i in range(1, int(sqrt(t)) + 1):
#         if t % i == 0:
#             fac.append(i)
#             fac.append(t // i)
#     for num in fac:
#         k = (num - a % num) % num
#         if gcd(a + k, t) < ans:
#             ans = gcd(a + k, t)
#             ansk = k
#
#     print(ansk)


a,b = map(int,input().split())
c = abs(a-b)
print(c-(a%c))