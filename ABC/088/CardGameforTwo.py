# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))


A = sorted(A)
Alice=[]
Bob=[]
for i in range(N):
    if i%2==0:
        Alice.append(A.pop())
    else:
        Bob.append(A.pop())

print(sum(Alice)-sum(Bob))
