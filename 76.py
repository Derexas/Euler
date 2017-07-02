import time, math

t = time.time()

result = 0
n = 6
tab = [0, 0, 1]

def ostuff(l, n):#, s):
	global result, tab
	if n < len(tab) and l <= n:
		result += tab[n] - tab[l]
		return
	m = l if l < n else n
	for i in range(1, m):
		ostuff(i, n - i)#, s + str(i))

for i in range(3, 100):
	ostuff(100000000, i)
	result += 1
	tab.append(result)
	result = 0
ostuff(100000000, 50)
print(tab)

print(result - 1, (time.time()-t)*1000)

"""
2 > 11 (1 + 0(1) - 0(0))
3 > 21.111 = (2)1 (1 + 1(2) - 0(1))
4 > 31.22.211.1111 = (3)1.(2)2 (1 + 2(3) - 0(1) + 1 + 1(2) - 1(2))
5 > 41.32.311.221.2111.11111 = (4)1.(3)2 (1 + 4(4) - 0(1) + 1 + 2(3) - 1(2))
6 > 51.42.411.33.321.3111.222.2211.21111.111111 = (5)1.(4)2.(3)3
(1 + 6(5) - 0(1) + 4(4) - 1(2) + 2(3) - 2(3))

"""
