# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

count = -1
loop_flag = True
while loop_flag:
    count = count + 1
    for i in range(N):
        if (A[i] % 2) == 0:
            A[i] = A[i] / 2
        else:
            loop_flag = False
    
print(count)
