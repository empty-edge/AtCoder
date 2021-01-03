# -*- coding: utf-8 -*-

N = int(input())
p = list(map(int, input().split()))

t = [0] * 210000
at = 0
for i in range(N):
    t[p[i]] = 1
    while t[at] > 0:
        at += 1

    print(at)
