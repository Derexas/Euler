import math, time

t = time.time()

def sieve(m):
    x = [True]*m
    x[0] = x[1] = False

    for i in range(2,int(math.sqrt(m))):
        j = 2*i
        while j < m:
            x[j] = False
            j = j+i

    return x

def primesinsieve(m):
    primes = []
    for i in range(len(m)):
        if m[i]:
            primes.append(i)
    return primes

def divisorsinprimes(m, p):
    d = [0]*m
    last = [1]*m
    for i in range(0,m,2):
    	last[i] += 1;
    for i in p:
        j = 2*i
        tt = (1 - 1/i)
        while j < m:
        	d[j] += (j/i)*last[j]
        	last[j] *= tt
        	j = j+i
        if i > m//2:
        	break
    for i in range(len(d)):
    	if d[i] > 0:
    		d[i] -= 1
    return d



result = 0 #539635574580 (dif between with 2 or not)

print(divisorsinprimes(14,[2,3,5,7,11,13]))

mm = 1000000
m = sieve(mm//2)
p = primesinsieve(m)
p.remove(2)
print(result, (time.time()-t)*1000)

d = divisorsinprimes(mm, p)

print((mm-1)*mm/2 - (sum(d) - 1))

"""
prer = 0
for i in range(len(d)):
    o = 1
    oo = 0
    for e in d[i]:
        b = (i/e)*o
        oo += b
        o *= (1 - 1/e)
    if oo > 0:
        oo -= 1
    prer += oo
print(prer)
result = (m-1)*m/2 - prer"""

"""
def isprime(x):
	prime = True
	for j in range(len(primes)):
		if x % primes[j] == 0:
			prime = False
			break
		elif x < primes[j] * primes[j]:
			break
	return prime

def isnotdivbysomeprimes(x):
	for someprime in someprimes:
		if x % someprime == 0:
			return False
	return True

def pdivisors(x):
	pds = []
	for j in range(len(primes)):
		if x % primes[j] == 0:
			pds.append(primes[j])
		elif x < primes[j]*primes[j]:
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
m = 87109/79180
M = 10000000//1

primes = [2]
for i in range(3,int(math.sqrt(M)),2):
	if isprime(i):
		primes.append(i)
someprimes = primes[1:2]
		
print((time.time()-t)*1000)
t = time.time()
"""

"""
for n in range(M-1, 87109, -2):
	if isnotdivbysomeprimes(n):
		pds = pdivisors(n)
		nl = nrelativep(n, pds)+1
		if n / nl < m and sorted(list(str(n))) == sorted(list(str(nl))):
			m = n / nl
			result = n
			print(n, n/m)
"""
"""
l = [2*x-1 for x in range(M//2)]

pp = primes[2:15]
for prime in pp:
	for n in range(0,M//2,prime):
		l[n] = False

for n in range(M//2 - 1, 1, -3):
	print(n, l[n])
"""

print(result, (time.time()-t)*1000)

