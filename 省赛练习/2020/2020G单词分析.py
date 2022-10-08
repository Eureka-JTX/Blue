s=input()
cnt=[0]*150
for i in s:
    cnt[ord(i)]+=1
print(chr(cnt.index(max(cnt))))
print(max(cnt))

    

