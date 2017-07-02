import time

t = time.time()

digits = [0,1,2,3,4,5,6,7,8,9]
primes = [2,3,5,7,11,13,17]

total = 0

def find(last, llast, ds, n, vx):
	global total
	for i in range(len(ds)):
		dss = list(ds)
		value = dss.pop(i)
		if (100*value + 10*last + llast) % primes[n] == 0 or len(dss) == 0:
			find(value, last, dss, n-1, vx*10 + value)
	if n == -2:
		pandiv = int(str(vx)[::-1])
		total += pandiv
		
for i in range(len(digits)):
	ds = list(digits)
	a = ds.pop(i)
	for i in range(len(ds)):
		dss = list(ds)
		b = dss.pop(i)
		find(a, b, dss, 6, 10*b + a)
	
print(total, time.time()-t)
