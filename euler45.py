
# Tn - T(n-1) = n(n+1)/2 - n(n-1)/2 = n
# Pn - P(n-1) = n(3n-1)/2 - (n-1)(3n-4)/2 = (-n + 7n-4)/2 = 3n - 2
# Hn - N(n-1) = n(2n-1) - (n-1)(2n-3) = -n + 5n-3 = 4n - 3

# T(n+1) = Tn + n
# P(n+1) = Pn + 3n - 2
# H(n+1) = Hn + 4n - 3

import time

t = time.time()

n = 166
m = 144
p = 40755 + 3*n - 2
h = 40755

while p != h:
	h += 4*m - 3
	while p < h:
		n += 1
		p += 3*n - 2
	m += 1
	
print(p, n, m, time.time()-t)
