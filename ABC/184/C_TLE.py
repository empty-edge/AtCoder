# -*- coding: utf-8 -*-
import math

def check(a,b,c,d):
    if a+b == c+d:
        return True
    if a-b == c-d:
        return True
    if abs(a-c) + abs(b-d) <= 3:
        return True
    return False

def get_dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

ans=0
px = x1
py = y1
while True:
    dist_min = get_dist(px, py, x2, y2)
    y_min = min(py, y2+1)
    y_max = max(py, y2+1)
    x_min = min(px, x2+1)
    x_max = max(px, x2+1)
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            if check(px, py, x, y) == True:
                dist = get_dist(x, y, x2, y2)
                if dist_min > dist:
                    next_px = x
                    next_py = y
                    dist_min = dist
    ans+=1
    if next_px==x2 and next_py==y2:
        break
    else:
        px = next_px
        py = next_py
        #print(px, py)

print(ans)
