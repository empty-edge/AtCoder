# -*- coding: utf-8 -*-

N,K = map(int, input().split())
LR = set()
for i in range(K):
    l,r = map(int, input().split())
    for val in range(l,r+1,1):
        LR.add(val)

count = [0] * N
count[0] = 1
for pos in range(N):
    if count[pos] > 0:
        for mv in LR:
            if pos + mv < N:
                count[pos+mv] += count[pos]
                #print(pos+1,mv)

ans = count[N-1] % 998244353
print(ans)