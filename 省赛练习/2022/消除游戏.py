def clean():
    global flag
    n = len(s)
    t = s[:]
    for i in range(n - 2):
        if t[i] == t[i + 1] and t[i + 1] != t[i + 2]:
            s[i + 1], s[i + 2] = 0, 0
        if t[i] != t[i + 1] and t[i + 1] == t[i + 2]:
            s[i + 1], s[i] = 0, 0
    m = s.count(0)
    if m == 0:
        flag = True
        return
    for _ in range(m):
        s.remove(0)


s = list(input())
flag = False
for _ in range(1 << 64):
    if flag:
        if len(s) == 0:
            print('EMPTY')
        else:
            print(''.join(map(str, s)))
        break
    clean()
