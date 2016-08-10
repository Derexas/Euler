import time

t = time.time()

num = 428571
den = 999999
m = 1
r = 3/8

while num > 1:
    while r < 3/7:
        r = num/den
        dif = 3/7 - r
        if dif < m:
            m = dif
            result = [num, den]
        den -= 1
    num -= 1

print(result, m, (time.time()-t)*1000)

# 428571/999999 = 3/7 ; 142857 fractions equals to 3/7 below 1M
