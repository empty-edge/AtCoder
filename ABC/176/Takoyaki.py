# -*- coding: utf-8 -*-

N,X,T =map(int, input().split())

cnt = int(N / X)
if N % X > 0:
    cnt += 1
t = cnt * T

print(t)