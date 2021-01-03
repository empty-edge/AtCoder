# -*- coding: utf-8 -*-

N = int(input())
list_t=[]
list_xy=[]
for i in range(N):
    t,x,y = map(int, input().split())
    list_t.append(t)
    list_xy.append([x,y])

goal = True
now_t = now_x = now_y = 0
for i,t in enumerate(list_t):
    diff_t = t - now_t
    dist = abs(list_xy[i][0] - now_x) + abs(list_xy[i][1] - now_y)
    if dist > diff_t or (dist + diff_t) % 2:
        goal = False
        break
    now_t = t
    now_x = list_xy[i][0]
    now_y = list_xy[i][1]

if goal:
    print("Yes")
else:
    print("No")
