# -*- coding: utf-8 -*-
 
N = int(input())
S = list(input())
 
password = set()
for i in range(1, N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            w = S[i-1] + S[j-1] + S[k-1]
            password.add(w)
 
print(len(password))