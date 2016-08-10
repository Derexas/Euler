import time

t = time.time()

# Long :(

def isprime(x):
	prime = True
	for j in range(len(primes)):
		if x % primes[j] == 0:
			prime = False
			break
		elif x < primes[j] * primes[j]:
			break
	return prime

primes = [2]
for i in range(3,30000,2):	
	if isprime(i):
		primes.append(i)

n = 1
b = 2
i = 1
p = 0
less10 = False
while not less10:
	for j in range(4):
		n += b
		if isprime(n):
			p += 1
	b += 2
	i += 4
	less10 = (p/i) < 0.1

print(b-1, (time.time()-t)*1000)