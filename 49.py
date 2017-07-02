
import time

t = time.time()

def isprime(x):
	prime = True
	for j in range(len(primes)):
		if x % primes[j] == 0:
			prime = False
			break
	return prime

def s(x):
	return sorted(list(str(x)))

primes = [2]
for i in range(3,150,2):	
	if isprime(i):
		primes.append(i)

answer = ''
digits = [1,2,3,4,5,6,7,8,9]
for i in range(len(digits)-7):
	ds = list(digits)
	a = ds.pop(i)
	for ii in range(len(ds)):
		dss = list(ds)
		b = dss.pop(ii)
		for iii in range(len(dss)):
			c = dss[iii]
			r = a*100+b*10+c
			if r != 148 and s(r) == s(r + 333) and s(r) == s(r + 666):
				r *= 10
				r3 = r + 3330
				r6 = r + 6660
				for i in range(1,10):
					if isprime(r+i) and isprime(r3+i) and isprime(r6+i):
						iii = ii = i = len(digits)
						answer = str(r+i)+str(r3+i)+str(r6+i)

print(answer, (time.time()-t)*1000)
