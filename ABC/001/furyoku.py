# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP

Deg, Dis = map(int, input().split())

Deg = Deg / 10

if 11.25 <= Deg and Deg < 33.75:
    Dir = "NNE"
elif 33.75 <= Deg and Deg < 56.25:
    Dir = "NE"
elif 56.25 <= Deg and Deg < 78.75:
    Dir = "ENE"
elif 78.75 <= Deg and Deg < 101.25:
    Dir = "E"
elif 101.25 <= Deg and Deg < 123.75:
    Dir = "ESE"
elif 123.75 <= Deg and Deg < 146.25:
    Dir = "SE"
elif 146.25 <= Deg and Deg < 168.75:
    Dir = "SSE"
elif 168.75 <= Deg and Deg < 191.25:
    Dir = "S"
elif 191.25 <= Deg and Deg < 213.75:
    Dir = "SSW"
elif 213.75 <= Deg and Deg < 236.25:
    Dir = "SW"
elif 236.25 <= Deg and Deg < 258.75:
    Dir = "WSW"
elif 258.75 <= Deg and Deg < 281.25:
    Dir = "W"
elif 281.25 <= Deg and Deg < 303.75:
    Dir = "WNW"
elif 303.75 <= Deg and Deg < 326.25:
    Dir = "NW"
elif 326.25 <= Deg and Deg < 348.75:
    Dir = "NNW"
else:
    Dir = "N"

v_str = Decimal(str(Dis / 60))
v = float(v_str.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

W = 0
if 0.3 <= v and v <= 1.5:
    W = 1
elif 1.6 <= v and v <= 3.3:
    W = 2
elif 3.4 <= v and v <= 5.4:
    W = 3
elif 5.5 <= v and v <= 7.9:
    W = 4
elif 8.0 <= v and v <= 10.7:
    W = 5
elif 10.8 <= v and v <= 13.8:
    W = 6
elif 13.9 <= v and v <= 17.1:
    W = 7
elif 17.2 <= v and v <= 20.7:
    W = 8
elif 20.8 <= v and v <= 24.4:
    W = 9
elif 24.5 <= v and v <= 28.4:
    W = 10
elif 28.5 <= v and v <= 32.6:
    W = 11
elif 32.7 <= v:
    W = 12

if W == 0:
    Dir = "C"

print(Dir, W)