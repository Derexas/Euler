import time

vs = [1,2,5,10,20,50,100,200]

def posforx(y):
	x = y
	b = 0
	while x > vs[b]:
		b+=1
	l = []
	total = 0
	t = 0
	a = x
	boo = True
	while boo:
		if total+vs[b] > x:
			b-=1
		if total == x or (b == 0):
			t+=1
			#print(l, total)
			if len(l) > 0:
				total-=l[-1]
				b = vs.index(l[-1])-1
				l.pop()
			else:
				print(t,'for',x)
				x = 0
				t = 0
				total = 0
				boo = False
		else:
			l.append(vs[b])
			total += vs[b]

t = time.time()
posforx(200)
t = time.time()-t
print(t*1000,"ms")
