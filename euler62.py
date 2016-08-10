import time

t = time.time()

result = 0

a = 10
n3dict = {}
for n in range(10000):
	n3 = n * n * n
	if n3 > a:
		a *= 10
	sln3 = list(str(n3))
	sln3.sort()
	sln3 = ''.join(sln3)
	if not sln3 in n3dict:
		n3dict[sln3] = [1, n3]
	else:
		n3dict[sln3][0] += 1
		if n3dict[sln3][0] == 5:
			result = n3dict[sln3][1]
			break

print(result, (time.time()-t)*1000)
