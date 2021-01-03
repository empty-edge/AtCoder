# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = a*500 + b*100 + c*50
            if total == X:
                count = count + 1

print(count)