import time

t = time.time()

blah = []
s = set()
n = 0

m = 10
for p in range(-1,-m,-1):
	for q in range(-p+1,m):
		r = (1 - p*q)/(p+q)
		if int(r) == r:
			a = int(p*q*r)
			blah.append([p, q, int(r), a])
			s.add(a)

if (len(blah) < 100):
	print(blah)
print(len(blah), len(s), time.time() - t)