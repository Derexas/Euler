import math, time

t = time.time()

ps = {}

for a in range(1,300):
	for b in range(1000,300,-1):
		c = math.sqrt(a**2 + b**2)
		if a + b + c <= 1000 and int(c) == c:
			key = str(a+b+int(c))
			if key in ps:
				ps[key] += 1
			else:
				ps[key] = 1	

result = ['0',0]
for tr in ps:
	if ps[tr] > result[1]:
		result = [tr, ps[tr]]
		
print(result, time.time()-t, 's')
	
