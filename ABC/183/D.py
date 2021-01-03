# -*- coding: utf-8 -*-

N, W = map(int, input().split())
t_max = (2 * (10**5) + 10)
cum = [0] * t_max
for i in range(N):
    s, t, p = map(int, input().split())
    cum[s] += p
    cum[t] -= p

for i in range(t_max-5):
    cum[i+1] += cum[i]
    if cum[i] > W:
        print("No")
        exit()

print("Yes")
