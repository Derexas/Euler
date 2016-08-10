import math, time

t = time.time()

def isprime(x):
	prime = True
	for j in range(len(primes)):
		if x % primes[j] == 0:
			prime = False
			break
		elif x < primes[j] * primes[j]:
			break
	return prime

def pdivisors(x):
	pds = []
	sqrt = int(math.sqrt(x))	
	for prime in primes:
		if x % prime == 0:
			pds.append(prime)
		elif sqrt < prime:
			break
	return pds

def nrelativep(x, pdivisors):
	nrp = 0
	odiv = 2
	old = 2
	for pd in pdivisors:
		a = x//pd
		old = (old - 1/odiv*old)
		a *= old
		nrp += a
		odiv = pd
	return nrp

result = 0
m = 0

M = 1000000

primes = [2]
for i in range(3,1020,2):
	if isprime(i):
		primes.append(i)

for n in range(2, M, 2):
	if n % 3 == 0 and n % 5 == 0:
		pds = pdivisors(n)
		nl = n - nrelativep(n, pds)
		if n / nl > m:
			m = n / nl
			result = n

print(result, result / m, (time.time()-t)*1000)

