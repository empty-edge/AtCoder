# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
a, b = map(int, input().split())

# 積
c = a * b

# 出力
if c % 2 > 0:
    print("Odd")
else:
    print("Even")