# -*- coding: utf-8 -*-
import math

N = int(input())

ans =  (10**N) - 9**N - 9**N + 8**N
ans = ans % ((10**9)+7)
print(ans)
