import time

vs = [1,2,5,10,20,50,100,200]
l = []

def posforx(y):
	x = y
	i = 0
	while x > vs[i]:
		i+=1
	u(x, i)
	l = []	
		
def u(a, b):
	total = 0
	t = 0
	x = a
	boo = True
	while boo:
		if total+vs[b] > x:
			b-=1
		else:
			#print(vs[b])
			l.append(vs[b])
			total += vs[b]
			if total == x:
				t+=1
				while len(l) > 1 and l[-1] == 1:
					l.pop()
					total-=1
				total-=l[-1]
				h = vs.index(l[-1])
				l.pop()
				if h > 0:
					b = h-1
				else:
					print(t,'for',x)
					x = 0
					t = 0
					total = 0
					boo = False

t = time.time()
posforx(200)
t = time.time()-t
print(t*1000,"ms")
