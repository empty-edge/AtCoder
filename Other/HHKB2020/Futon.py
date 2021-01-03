# -*- coding: utf-8 -*-

def check(S, H, W, x, y):
    cnt = 0
    if S[y][x] == '.':
        if x+1 < W and S[y][x+1] == '.':
            cnt += 1
        if y+1 < H and S[y+1][x] == '.':
            cnt += 1

    return cnt

H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))

ans = 0
for y in range(H):
    for x in range(W):
        cnt = check(S, H, W, x, y)
        ans += cnt

print(ans)

