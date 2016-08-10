import math, time

t = time.time()

def msum(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s
	
def dostuff(a):
	global oold, old, new
	oold = old
	old = new
	new = oold+old*a

result = 0

old = 3
new = 8
a = 4
for i in range(4, 101, 3):
	dostuff(1)
	dostuff(1)
	dostuff(a)
	a += 2
result = msum(oold)

print(result, (time.time()-t)*1000)
