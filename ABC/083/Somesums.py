# -*- coding: utf-8 -*-

N,A,B = map(int, input().split())

total = 0
for i in range(1,N+1):
    x = str(i)
    num = 0
    for j in range(len(x)):
        num = num + int(x[j])

    if A<=num and num<=B:
        total = total + i

print(total)