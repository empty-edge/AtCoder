# -*- coding: utf-8 -*-
 
N = int(input())
S = list(input())
 
sumtmp = [[0 for i in range(N) ] for j in range(10)]
sumtmp[int(S[0])][0] = 1
for i in range(1, N):
    val = int(S[i])
    for j in range(10):
        sumtmp[j][i] = sumtmp[j][i-1] 
        if j == val:
            sumtmp[j][i] += 1
 
pw = set()
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(10):
            if sumtmp[k][N-1] - sumtmp[k][j] > 0:
                w = S[i]+S[j]+str(k) 
                pw.add(w)
 
print(len(pw))