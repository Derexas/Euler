import math, time

t = time.time()

def process(intv, n, val, n_mult):
	denum = (n - val * val) / n_mult
	a = 0
	while val-denum >= -intv:
		val -= denum
		a += 1
	val = -val
	return [a, val, denum] #intv, val, n_mult

result = 0

for n in range(10000):
	sqrt = math.sqrt(n)
	a = int(sqrt)
	if sqrt - a > 0:
		intv = a
		afirst = process(a, n, a, 1)
		i = 1
		r = afirst
		while True:
			r = process(intv, n, r[1], r[2])
			if r == afirst:
				break			
			i += 1
		if i % 2 != 0:
			result += 1

print(result, (time.time()-t)*1000)
