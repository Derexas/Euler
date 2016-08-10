
# 1 > 1
# 2 > 2,4,8,6,2
import time
t = time.time()

sum = 0
for i in range(1,1000):
	sum += i**i
print(str(sum)[-10:], (time.time()-t)*1000)