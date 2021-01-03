# -*- coding: utf-8 -*-

def comp_word(w1, w2, len):
    cnt = len
    for i,w in enumerate(w1):
        if w == w2[i]:
            cnt -= 1
    
    return cnt


def main(S, T):
    T_len = len(T)
    cnt_min = T_len
    for i in range(len(S)-T_len+1):
        sub_S = S[i:i+T_len]
        if len(sub_S) == T_len:
            cnt = comp_word(sub_S, T, T_len)
            if cnt < cnt_min:
                cnt_min = cnt 

    print(cnt_min)


S = input()
T = input()
main(S, T)
