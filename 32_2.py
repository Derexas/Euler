import time

t = time.time()

l = set()
digits = ['1','2','3','4','5','6','7','8','9']
a = [0,0]
for m1 in range(1,100):
	for m2 in range(int(10000/m1)):
		product = m1 * m2
		if product < 10000 and product > 1000:
			a[0]+=1
			string = str(m1) + str(m2) + str(product)
			if len(string) == 9 and sorted(list(string)) == digits:
				l.add(product)
		else:
			a[1]+=1
				
print(sum(l), time.time()-t, 's', a)
