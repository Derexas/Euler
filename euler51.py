
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

def processPos(l, stuff, n):
	global posll
	if n > 0:
		for i in range(len(l)):
			s = list(stuff)
			s.append(l[0])
			processPos(list(l), s, n-1)
			l.pop(0)
	else:
		posll.append(stuff)

def createandcheck(poslist, sn):
	a = r = 0
	b = 1 if poslist[0] == 0 else 0
	for n in range(b,10):
		decal = 0
		snn = str(sn)
		for el in poslist:
			snn = snn[:el+decal]+ str(n) +snn[el+decal:]
			decal += 1
		if n - a > 2:
			break
		if isprime(int(snn)):
			if a == 0:
				r = snn
			a += 1
	if a >= 8:
		print('Yay', sn, r)
		return True


primes = [2]
for i in range(3,1500,2):
	if isprime(i):
		primes.append(i)

posll = [[0]]

n = 1
found = False
while not found:
	sn = str(n)
	m = len(sn)
	if m > len(posll[-1]):
		posll = []
		for i in range(1, m+1):
			processPos(list(range(m)), list(), i)
	for posl in posll:
		if createandcheck(posl, sn):
			found = True
			break
	n += 2

print((time.time()-t)*1000)
