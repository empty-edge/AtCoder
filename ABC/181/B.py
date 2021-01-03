# -*- coding: utf-8 -*-

N = int(input())
ans = 0
for i in range(N):
    A, B = map(int, input().split())
    ans = ans + int((A+B)*(B-A+1)*0.5)

print(int(ans))