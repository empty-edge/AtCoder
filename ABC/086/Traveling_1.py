# -*- coding: utf-8 -*-

def get_next_pos(now_pos, next_pos):
    for mv in [[-1,0],[1,0],[0,-1],[0,1]]:
        next_x = now_pos[0] + mv[0]
        next_y = now_pos[1] + mv[1]
        if [next_x, next_y] not in next_pos:
            next_pos.append([next_x, next_y])
    
    return next_pos

def get_candidate_pos(now_pos, length):
    for t in range(length):
        next_pos = []
        for pos in now_pos:
            next_pos = get_next_pos(pos, next_pos)

        now_pos = next_pos

    return now_pos

N = int(input())
list_t=[]
target_pos=[]
for i in range(N):
    t,x,y = map(int, input().split())
    list_t.append(t)
    target_pos.append([x,y])

goal = True
now_t = 0
now_pos = [[0, 0]]
for i,t in enumerate(list_t):
    length = t - now_t
    now_pos = get_candidate_pos(now_pos, length)
    #print(now_pos)
    if target_pos[i] not in now_pos:
        goal = False
        break
    
    now_t = t

if goal:
    print("Yes")
else:
    print("No")
