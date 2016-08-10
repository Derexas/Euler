import time

t = time.time()

pentas = [1,5]
n = 3
d = 1000

while n < 10000:
	penta = pentas[n-2] + 3*n - 2 #int(n * (3*n - 1)/2)
	i = n - 2
	while pentas[i] > penta/2:
		op = pentas[i]
		if penta - op in pentas and 2*op - penta in pentas: # and penta - op < d:
			print(penta, op, penta - op, 2*op - penta, int(time.time()-t))
		i -= 1
	pentas.append(penta)
	n += 1
	
"""
Test each new found penta with the ones preceding it
By some luck the first okay penta was the one needed
"""
