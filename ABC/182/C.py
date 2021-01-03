# -*- coding: utf-8 -*-

def func(N, bit):
    ret = ""
    delete_cnt = 0
    for i in range(len(N)):
        if bit[i] == 1:
            ret += N[i]
        else:
            delete_cnt += 1
    return ret, delete_cnt

N = input()

ans = -1
cnt_min = 10**18
num = len(N)
for i in range(1<<num):
    bit = [0] * num
    for j in range(num):
        div = 1 << j
        bit[j] = (i // div) % 2
    
    val, cnt = func(N, bit)
    if cnt < num:
        if int(val) % 3 == 0:
            if cnt < cnt_min:
                ans = cnt
                cnt_min = cnt

print(ans)
