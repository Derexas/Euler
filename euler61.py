import time

t = time.time()

# Triangle: 1000 = n(n+1)/2 ; 2000 = n(n+1) ; n = 45 ;; 19998 = n(n+1) ; n = 141
# Square:	1000 = n² ; n = 32 ;; 9999 = n² ; n = 100
# Pentagon:	1000 = n(3n-1)/2 ; 3n²-n-2000 = 0 ; n = 23 ;; 3n²-n-19998 = 0 ; n = 82
# Hexagon:	
# abcd cdef efgh ghij ijkl klab : 10^(6*4 - 2) = 10^22 = 100M of M of B

def processp(f):
	n = 0
	pn = 1
	p = []
	while pn < 1000:
		pn = int(f(n))
		n += 1
	while pn < 9999:
		p.append(pn)
		pn = int(f(n))
		n += 1
	return p
	
def find(st, li, l):
	global result
	if len(li) > 0:
		for i in li:
			lli = list(li)
			lli.remove(i)
			for n in stuff[i]:
				if n[:2] == st:
					ll = list(l)
					ll.append(n)
					if find(n[2:], lli, ll):
						return True
	elif l[-1][2:] == l[0][:2]:
		result = sum(map(int, l))
		return True
	
result = 0
	
triangles = processp(lambda n: n*(n+1)/2)
squares = processp(lambda n: n*n)
pentagons = processp(lambda n: n*(3*n-1)/2)
hexagons = processp(lambda n: n*(2*n-1))
heptagons = processp(lambda n: n*(5*n-3)/2)
octogons = processp(lambda n: n*(3*n-2))

stuff = [triangles, squares, pentagons, hexagons, heptagons, octogons]

for p in stuff:
	for i in range(len(p)):
		p[i] = str(p[i])
		
li = [i for i in range(len(stuff)-1, 0, -1)]
for n in stuff[-1]:
	if find(n[2:], li, [n]):
		break

print(result, (time.time()-t)*1000)

