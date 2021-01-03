# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)  # RecursionError対策

def func(n, h):
    if n == 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    
    res = 10**10
    res = min(res, func(n-1, h) + abs(h[n]-h[n-1]))
    if n > 1:
	    res = min(res, func(n-2, h) + abs(h[n]-h[n-2]))

    memo[n] = res
    return res

N = int(input())
h = list(map(int, input().split()))

memo = [-1] * (N+1)
ans = func(N-1, h)
print(ans)
