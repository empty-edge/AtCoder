# -*- coding: utf-8 -*-

A,B,C,X,Y = map(int, input().split())

# AB only
yen1 = max(X,Y) * 2 * C

# A + AB
yen2 = (max(X-Y, 0) * A) + (Y * 2 * C)

# AB + B
yen3 = (X * 2 * C) + (max(Y-X, 0) * B)

# A + B
yen4 = X * A + Y * B

ans = min(yen1, yen2, yen3, yen4)
print(ans)
