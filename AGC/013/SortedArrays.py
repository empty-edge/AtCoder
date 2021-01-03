# -*- coding: utf-8 -*-

def check(A,i,j):
    tmp = []
    for k in range(i,j):
        tmp.append(A[k])

    print(tmp)

N = int(input())
A = list(map(int, input().split()))

cnt = i = 0
while True:
    flag = 0
    for j in range(i+1,N):
        if flag == 0:
            if A[i] < A[j]:
                flag = 1
            elif A[i] > A[j]:
                flag = -1
        else:
            if flag == 1:
                if A[j-1] > A[j]:
                    #check(A,i,j)
                    i = j
                    cnt += 1
                    break
            elif flag == -1:
                if A[j-1] < A[j]:
                    #check(A,i,j)
                    i = j
                    cnt += 1
                    break
    else:
        cnt += 1
        break

    if i>=N:
        break

print(cnt)
    