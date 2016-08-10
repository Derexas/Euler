import math, time

t = time.time()

# r!(n-r)! (max when r = n/2)

def c(n, r):
	return facts[n]/(facts[r]*facts[n - r]) > 1000000

facts = [math.factorial(i) for i in range(0, 101)]

result = 0
for n in range(23,101):
	r = int(n/2)
	if c(n, r):
		result += 1
		if n % 2 == 0:
			result += 1
		d = 1
		while c(n, r - d):
			result += 2
			d += 1

print(result, (time.time()-t)*1000)

