import time

t = time.time()

result = 0

n = 1
d = 10
a = 1
oldr = -1
while oldr != result:
	oldr = result
	while a**n < d:
		a += 1
		result += 1
	n += 1
	while a**n > d:
		a -= 1
	a += 1
	d *= 10

print(result, (time.time()-t)*1000)
