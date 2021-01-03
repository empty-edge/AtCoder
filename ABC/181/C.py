# -*- coding: utf-8 -*-
import math

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

N = int(input())
p = []
for i in range(N):
    x,y = map(int, input().split())
    p.append([x,y])

for i in range(N):
    for j in range(i+1, N):
        dist_ij = get_distance(p[i][0], p[i][1], p[j][0], p[j][1])
        for k in range(j+1, N):
            dist_ik = get_distance(p[i][0], p[i][1], p[k][0], p[k][1])
            dist_jk = get_distance(p[j][0], p[j][1], p[k][0], p[k][1])
            a = (dist_ij + dist_ik) - dist_jk
            b = (dist_ij + dist_jk) - dist_ik
            c = (dist_ik + dist_jk) - dist_ij
            if a<0.1e-10 or b<0.1e-10 or c<0.1e-10:
                print("Yes")
                exit() 

print("No")
