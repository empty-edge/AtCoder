# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

p = [0] * N
q = [0] * N
q_max = tmp = 0
for i in range(N):
    tmp += A[i]
    p[i] = tmp
    if tmp > q_max:
        q_max = tmp

    q[i] = q_max

r = x = 0
for i in range(N):
    r = max(r, x + q[i])
    x = x + p[i]

print(r)
