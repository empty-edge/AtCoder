# -*- coding: utf-8 -*-

N = int(input())
h = list(map(int, input().split()))

cost = [10**10] * (N+1)
cost[0] = 0
for i in range(N):
    if i+1 < N:
        total_cost = abs(h[i]-h[i+1]) + cost[i]
        cost[i+1] = min(cost[i+1], total_cost)
    if i+2 < N:
        total_cost = abs(h[i]-h[i+2]) + cost[i]
        cost[i+2] = min(cost[i+2], total_cost)

ans = cost[N-1]
print(ans)
