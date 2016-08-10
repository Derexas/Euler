import time, math

t = time.time()

i = 16
l = []
d = result = 0
while True:
	a = str(i)[-1]
	#l.append(a)
	if a == '0' and l[len(l)-2] == '8' and l[len(l)-3] == '4' and l[len(l)-4] == '2' and l[len(l)-5] == '1':
		if d == 1:
			result = i
			break
		else:
			d = 1
	#print (a)
	i *= 2
print(''.join(l))

# 24862486 4 (4)
#   11  11  11  11
#  00136251249986375 (20)
#      1 1   1111 11
#   000012500013750125136248749862513749875124863636249999874
#	99986249874863751250137486250124875136363750000 12500 (100)

p = 7830457
y = 22, yend = 4
while :
	a = p % y
	p -= a

print(result, (time.time() - t)*1000)