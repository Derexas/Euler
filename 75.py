import time, math

t = time.time()

result = 0
M = 1500000//1000
squares = [i*i for i in range(M)]
can = [False for i in range(M)]
for i in range(1, len(squares)):
    sq = squares[i]
    d = 0
    for j in range(i, len(squares)):
        sqq = squares[j]
        r = sq + sqq
        if r in squares:
            d += 1
            """a = int(math.sqrt(sq))
            b = int(math.sqrt(sqq))
            c = int(math.sqrt(r))
            print(a + b + c, a, b, c)"""
            if d > 1:
                break
    if d == 1:
        result += 1

print(result, (time.time()-t)*1000)

"""
1,500,000 > 

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

12*2 > 36 ; 20*2 > 40 ; 12*3 > 48 ; ..
"""
