import math, time

t = time.time()

def solve(D):
	a = int(math.sqrt(D))
	if (a+1)**2 - D < -(a**2 - D):
		a += 1
	b = 1
	k = a**2 - D
	pk = k if k > 0 else -k
	while not (k == 1 and int(a) == a and int(b) == b):
		d = 0
		stuff = a + b*d
		while stuff != (stuff//pk)*pk:
			d += 1
			stuff += b
		i = 0 #|m²-D| must be minimal
		m = pk*i + d
		r1 = m*m - D
		r1 = r2 = r1 if r1 > 0 else -r1
		while r1 <= r2:
			i += 1
			m = pk*i + d
			r2 = r1
			r1 = m*m - D
			r1 = r1 if r1 > 0 else -r1
		m = m if r1 < r2 else pk*(i - 1) + d
		
		aa = (a*m + D*b)//pk
		b = (a + b*m)//pk
		a = aa
		kf = (m*m - D)/k
		k = (m*m - D)//k
		pk = k if k > 0 else -k
		#print(a,b, 'k:'+str(k), 'm:'+str(m), 'd:'+str(d), kf)
	#print(D, a,b,k)
	return a

result = m = 0

L = 1000

l = [x for x in range(2, L)]
i = 2
ii = i * i
while ii < L:
	l.pop(ii - i)
	i += 1
	ii = i*i

for D in l:	
	a = solve(D)
	if a > m:
		m = a
		result = D

print(result, m, (time.time()-t)*1000)
