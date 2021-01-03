# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

max_A = min_A = A[0]
for i in range(1,N,1):
    if A[i] > max_A:
        max_A = A[i]
    if A[i] < min_A:
        min_A = A[i]

max_diff = max_A - min_A
print(max_diff)
