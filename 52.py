
import time
#1(<7)
#l >= 6
#0 with x2: void (from other) so no 0
#1 with x2: 5*2+1 (or 0*2+1 but nope because no 0)
#5 with x2: 2*2+1
#2 with x2: 6*2 (or 1*2 but it loops so don't work for 1rst 1)
#6 with x2: 3*2
#3 with x2: 1*2+1 or 6*2+1
#4 with x2: 2*2
#8 with x2: 4*2
#9 with x2: 4*2+1

# 1 > 5 > 2 > 1 or 6
# 6 > 3 > 2 > 1 or 6..
# 7 > 8 > 4 > 2..
# 9 > 4 > 2..

#1 x3: 3*3+2			1 > 3 and (>=7)
#2 x3: 3*4				2 > 4
#3 x3: 3*1 or 3*4+1		3 > 4 or 1
#4 x3: 3*1+1 or 3x4+2 	4 > 3 or 4
#5 x3: 3*5 or 3*1+2		5 > 5 or 1
#6 x3: 3*5+1 or 3*2		6 > 5 or 2
#7 x3: 3*2+1 or 3*5+2	7 > 5 or 2
#8 x3: 3*2+2 or 3*6		8 > 6 or 2
#9 x3: 3*3 or 3*6+1 	9 > 6 or 3

#1 x6: 6*9 or ...
"""
	strn = str(n)
	if strn[0] != '1':
		n = 10**(len(n+1))
"""

t = time.time()

n = 123456 - 1
found = False
while not found:
	n += 1
	digits = set(str(n))
	found = True
	for mult in range(2,7):
		if not set(str(n * mult)) == digits:
			found = False
			break

print(n, (time.time()-t)*1000)
