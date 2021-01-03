# -*- coding: utf-8 -*-

def count(val1, val2):
    count = 1
    while True:
        if val1 < (val2 ** count):
            res = 0
            if count > 1:
                res = val2 ** (count-1)

            break  
        count += 1

    return res


N = int(input())
left = N
ans = 0
while True:
    num1 = count(left, 9)
    num2 = count(left, 6)
    if num1==0 and num2==0:
        break

    print(left,num1,num2)
    if num1 > num2:
        left = left - num1
    else:
        left = left - num2

    ans += 1


print(left,ans)
ans += left

print(ans)