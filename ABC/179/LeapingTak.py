# -*- coding: utf-8 -*-
MOD = 998244353
N,K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]

dp = [0] * N
dp[0] = 1
sumdp = [0] * N
sumdp[0] = 1
for i in range(1,N):
    for l, r in LR:
        if i-r-1>=0:
            dp[i] += sumdp[i-l] - sumdp[i-r-1]
        elif i-l >= 0:
            dp[i] += sumdp[i-l]
        dp[i] = dp[i] % MOD

    sumdp[i] = sumdp[i-1] + dp[i]

ans = dp[N-1]
print(ans)