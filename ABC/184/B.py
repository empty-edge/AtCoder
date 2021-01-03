# -*- coding: utf-8 -*-

N, X = map(int, input().split())
S = input()

ans = X
for i in range(N):
    if S[i] == "o":
        ans += 1
    elif S[i] == "x":
        if ans > 0:
            ans -= 1

print(ans)