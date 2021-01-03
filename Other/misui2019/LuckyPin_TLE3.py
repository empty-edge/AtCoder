# -*- coding: utf-8 -*-
 
N = int(input())
S = input()
 
ans = 0
for i in range(1000):
    pw = list("{0:03d}".format(i))
 
    w1 = -1
    for j in range(N-2):
        if S[j] == pw[0]:
            w1 = j
            break
    if w1 == -1:
        continue
 
    w2 = -1
    for j in range(w1+1, N-1):
        if S[j] == pw[1]:
            w2 = j
            break
    if w2 == -1:
        continue
 
    w3 = -1
    for j in range(w2+1, N):
        if S[j] == pw[2]:
            w3 = j
            break
    if w3 == -1:
        continue
 
    ans += 1
 
print(ans)