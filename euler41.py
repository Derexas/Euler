import math, time

def isprime(x):
	m = int(math.sqrt(x))+1
	for i in range(3,m,2):
		if x%i == 0:
			return False
	return True
	
t = time.time()

digits = [1,2,3,4,5,6,7]#,8,9]
bigprime = 0

def pangen(ds, n, pan):
	global bigprime
	for i in range(0,len(ds), 2 if n == 0 else 1):
		l = list(ds)
		v = l.pop(i)
		p = pangen(l, n+1, 10**n * v + pan)
	if n == len(digits):
		if isprime(pan) and pan > bigprime:
			bigprime = pan
	return False
		
for i in range(7):
	p = pangen(list(digits),0,0)
	digits.pop()
	
print(bigprime, time.time()-t)
