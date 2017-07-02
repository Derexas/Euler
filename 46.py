
import math, time

t = time.time()

primes = [2,3]
n = 5
found = False
while not found:
	i = 0
	prime = True
	while prime and n > primes[i]**2:
		prime = n % primes[i] != 0
		i += 1
	if prime:
		primes.append(n)
	else:
		found = True
		for i in range(len(primes)):		
			a = math.sqrt((n-primes[i])/2)
			if a == int(a):
				found = False
				break
	n += 2
		
print(n - 2, (time.time()-t)*1000)
			
