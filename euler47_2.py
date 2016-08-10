
import time

t = time.time()

primes = [2]
n = 3
while len(primes) < 500:
	prime = True
	i = 0
	while n > primes[i]**2:
		i += 1
		if n % primes[i] == 0:
			prime = False
			break
	if prime:
		primes.append(n)
	n += 2
	
qpdivid = []
limit = 1000000

for i in range(len(primes)):
	for j in range(i,len(primes)):
		for k in range(j,len(primes)):
			for l in range(k,len(primes)):
				r = 
found = False
n = 6
while not found:
	n += 1
	if has4primediv(n):
		if has4primediv(n+1) and has4primediv(n+2) and has4primediv(n+3):
			found = True
		else:
			pass#n += 3

print(n, (time.time()-t)*1000)
