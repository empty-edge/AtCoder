# -*- coding: utf-8 -*-
import math

N = int(input())

ans = 0
N_half = int(math.sqrt(N))
for A in range(1, N_half+1):
    for B in range(1, N):
        if A * B < N:
            ans += 1
            if B > N_half:
                ans += 1
        else:
            break
    
print(ans)
 