import time

digitss = [1,2,3,4,5,6,7,8,9]
l = set()
sss = 0
def op(digits, s=""):
	global l, sss
	for i in range(len(digits)):
		d = list(digits)
		del d[i]
		if len(d) > 0:
			op(d, s+str(digits[i]))
		else:
			ss = s+str(digits[i])
			n1 = int(ss[:2])
			n2 = int(ss[2:5])
			n3 = int(ss[5:])
			if n1*n2 == n3:
				l.add(n3)
			n1 = int(ss[:1])
			n2 = int(ss[1:5])
			n3 = int(ss[5:])
			if n1*n2 == n3:
				l.add(n3)
			
t = time.time()
op(digitss)
sum = 0
for i in l:
	sum += i
print(sum, time.time()-t, 's')

"""
12 483 5796
18 297 5346
27 198 5346
28 157 4396
39 186 7254
42 138 5796
48 159 7632
"""
