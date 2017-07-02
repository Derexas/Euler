import time

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
	
result = 0

primesgrp = []
primes = [2]
strprimes = ['2']
for i in range(3,10000,2):
	if isprime(i):			
		primes.append(i)
		strprimes.append(str(i))

a = 0
while a < len(strprimes):
	prime = strprimes[a]
	primesgrp.append([prime])
	b = 0
	while b < len(strprimes):
		p = strprimes[b]
		if p != prime:
			okay = True
			for pp in primesgrp[-1]:
				if not isprime(int(p + pp)) or not isprime(int(pp + p)):
					okay = False
					break
			if okay:
				primesgrp[-1].append(p)
			if len(primesgrp[-1]) == 5:
				#print(primesgrp[-1])
				a = b = 100000
				result = sum(map(int, primesgrp[-1]))
				break
		b += 1
	a += 1

print(result, (time.time()-t)*1000)
