# -*- coding: utf-8 -*-

    if a+b == c+d:
        return True
    if a-b == c-d:
        return True
    if abs(a-c) + abs(b-d) <= 3:
        return True
    return False


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x = x2 - x1
y = y2 - y1
if x==0 and y==0:
    ans = 0
elif x1+y1 == x2+y2:
    ans = 1
elif x1-y1 == x2-y2:
    ans = 1
elif abs(x1-x2) + abs(y1-y2) <= 3:
    ans = 1

