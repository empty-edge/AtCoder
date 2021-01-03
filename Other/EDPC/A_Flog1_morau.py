# -*- coding: utf-8 -*-

N = int(input())
h = list(map(int, input().split()))

cost = [10**10] * (N+1)
cost[0] = 0
for i in range(1,N):
    cost[i] = cost[i-1] + abs(h[i]-h[i-1])
    if i > 1:
        tmp = cost[i-2] + abs(h[i]-h[i-2])
        cost[i] = min(cost[i], tmp)

ans = cost[N-1]
print(ans)
