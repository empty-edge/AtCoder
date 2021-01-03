# -*- coding: utf-8 -*-
import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

seq =  [i for i in range(1, N) ]
comb_list = list(itertools.permutations(seq))

ans = 0
for comb in comb_list:
    seq = (0,) + comb + (0,)
    cost = 0
    for i in range(len(seq)-1):
        s = seq[i]
        e = seq[i+1]
        cost += T[s][e]
    if cost == K:
        ans += 1

print(ans)