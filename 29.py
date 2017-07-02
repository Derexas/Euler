import math

a_min = 2
a_max = 100
b_min = 2
b_max = 100
result = 0
"""
# 2>4>8>16>32>64
# 3>9>27>81
# 5>25
# 6>36
# 7>49
# 10>100
"""
r = []
for i in range(a_min,a_max+1):
	for j in range(b_max,b_min-1, -1):
		rr = math.pow(i,j)
		if not rr in r:
			r.append(rr)
			result+=1
print(result)
"""
2^100 = 4^50 = 16^25 = 32^20 ~= 8^34 = 64^17
3^100 = 9^50 = 81^25 ~= 27^34
5^100 = 25^50
6^100 = 36^50
7^100 = 49^50
10^100 = 100^50
"""
