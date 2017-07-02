"""
28433×2^7830457+1
find the last 10 digits of that number
1 2 3  4  5
2 4 8 16 32 64 128 256 512
7830457 % 4 = 1 -> ends with 2
2^7830457 = (2^7830457)^
"""
import math
import time
from functools import reduce

start = time.time()

bign = 10**10
l = []
l2 = []
l3 = []
aa = 7830457
while aa > 0:
	a = int(math.log2(aa))
	l.append(a)
	b = 2**a
	c = b % bign
	l2.append(c)
	l3.append(2**c % bign)
	aa -= b

p = 1
for n in l3:
	p *= n
d = p % bign
e = (28433*d + 1)%bign

end = time.time()
print((end - start)*1000)

print(e)

# apparently python just take whatever you throw at it..
# print((28433 * (2**7830457) + 1)%10000000000) # <- works