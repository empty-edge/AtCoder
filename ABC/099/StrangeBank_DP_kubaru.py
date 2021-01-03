# -*- coding: utf-8 -*-

N = int(input())

max_n = 110000
dp = [N] * max_n
dp[0] = 0

for n in range(N):
    pow6 = 1
    while n + pow6 <= N:
        dp[n+pow6] = min(dp[n+pow6], dp[n]+1)
        pow6 *= 6

    pow9 = 1
    while n + pow9 <= N:
        dp[n+pow9] = min(dp[n+pow9], dp[n]+1)
        pow9 *= 9

print(dp[N])
