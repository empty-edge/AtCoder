# -*- coding: utf-8 -*-

S = list(input())

if S[len(S)-1] == "s":
    ans = "".join(S) + "es"
else:
    ans = "".join(S) + "s"

print(ans)