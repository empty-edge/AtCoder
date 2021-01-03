# -*- coding: utf-8 -*-

D,T,S = map(int, input().split())

cost_t = D  / S
if T >= cost_t:
    print('Yes')
else:
    print('No')
