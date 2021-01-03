# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

diff_sum = 0
for i in range(N-1):
    if A[i+1] < A[i]:
        diff = A[i] - A[i+1] 
        diff_sum += diff
        A[i+1] += diff


print(diff_sum)

