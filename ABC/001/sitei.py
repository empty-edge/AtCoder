# -*- coding: utf-8 -*-

m = int(input())

ans = ""
if m < 100:
    ans = "00"
elif 100 <= m and m <=5000:
    tmp = m // 100
    if len(str(tmp))==1:
        ans = "0" + str(tmp)
    else:
        ans = tmp
elif 6000 <= m and m <= 30000:
    ans = m // 1000 + 50
elif 35000 <= m and m <= 70000:
    ans = (m // 1000 - 30) // 5 + 80
elif m > 70000:
    ans = 89

print(ans)
