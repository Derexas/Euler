import time

t = time.time()

result = 0
a = [3,2]
b = [7,5]
d = 10
for i in range(3,1000):
	c = list(b)
	b[0] = 2*b[0] + a[0]
	b[1] = 2*b[1] + a[1]
	a = c
	if b[0] > d:
		if b[1] < d:
			result += 1
		d *= 10

print(result, (time.time()-t)*1000)