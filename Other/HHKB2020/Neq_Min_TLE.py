# -*- coding: utf-8 -*-

N = int(input())
p = list(map(int, input().split()))

for i in range(N):
    p_sorted = list(set(sorted(p[0:i+1])))
    res = -1
    num = len(p_sorted)
    for j in range(num):
        if p_sorted[j] != j:
            res = j
            break
    if res == -1:
        res = p_sorted[num-1] + 1

    print(res)