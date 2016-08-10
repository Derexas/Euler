import time

t = time.time()

numbers = []
result = 0
for n in range(9999,1,-1):
	lychrel = True
	a = 1
	b = n + int(str(n)[::-1])
	while lychrel and a < 50:
		inv = int(str(b)[::-1])
		if inv == b:
			lychrel = False
		else:
			b = inv + b
		a += 1
	if lychrel:
		result += 1

print(result, (time.time()-t)*1000)