# -*- coding: utf-8 -*-

sx, sy, gx, gy = map(int, input().split())

gy = -gy
a = (gy - sy) / (gx - sx)
b = sy - a * sx

print(b/a*-1)