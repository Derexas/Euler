import time

t = time.time()

m = 0
for a in range(100):
	for b in range(10,100):
		c = a**b
		r = sum(map(int, str(c)))
		if r > m:
			m = r

print(m, (time.time()-t)*1000)