# -*- coding: utf-8 -*-
N = int(input())
A_list = []
B_list = []
for i in range(N):
    A,B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

ans = N*(10 ** 10) 
for A in A_list:
    for B in B_list:
        res = 0
        for i in range(N):
            res += abs(A_list[i]-A)
            res += abs(B_list[i]-B)
            res += abs(A_list[i]-B_list[i])

        ans = min(ans, res)

print(ans)