# -*- coding: utf-8 -*-

N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d_unique = list(set(d))

print(len(d_unique))