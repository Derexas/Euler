"""

"""

from itertools import combinations_with_replacement
import math
import time


start = time.time()

count = 0
digits = [i for i in range(0,10)]
sqrs = [i**2 for i in digits]


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def sum_sqdigits(n):
	s = 0
	while n:
		s, n = s + sqrs[n % 10], n // 10
	return s

# pre-process all the possible nCr which are going to be used
ncrs = [[0]*10 for _ in range(10)]
for n in range(10):
	for r in range(n):
		ncrs[n][r] = nCr(n, r)

n, r = len(digits), 7
# number of combinations with repetitions
ncwr = math.factorial(n+r-1)/(math.factorial(r)*math.factorial(n-1))
# number of combinations
nc = math.factorial(r)

n, k = digits, r
# get a list of all combinations with replacement
cwr = list(combinations_with_replacement(n,k))

sqs = [0]*len(cwr) #contains the sum of square digits of each set from cwr
rs = [0]*len(cwr) #number of numbers made out of each set from cwr ((1,2) > 12,21:2)
repets = [[0]*10 for i in cwr] #number of time a digits is present in each set
i = 0
for c in cwr:
	for b in c:
		repets[i][b] += 1
		sqs[i] += sqrs[b]
	i += 1

maxssq = (r*9**2 + 1) #max sum of sq digits of numbers bellow 10M
yn = [-1]*maxssq #array of whether a number 'goes' to 89 or not (-1 if unknow)
yn[89] = True
yn[0] = yn[1] = False #set them at False because they 'loop'

i = 0
for sq in sqs: #for each sum of square digits
	originalsq = sq
	# process rs[i]
	ccc = r
	cc = 1
	for rr in repets[i]:
		cc *= nCr(ccc, rr)
		ccc -= rr
	rs[i] = cc
	# if True, update count
	if yn[sq] == True:
		count += rs[i]
	# if maybe True..
	if yn[sq] == -1:
		m = []
		#..process the digits sums until being sure
		while yn[sq] == -1:
			sq = sum_sqdigits(sq)
			m.append(sq)
		if yn[sq] == True:
			count += rs[i] #update count
			for osq in m: #set all the previous parsed numbers to True
				yn[osq] = True
			#print(originalsq, rs[i], cwr[i], m, repets[i], i)
	i += 1

print(count)

end = time.time()
print((end - start)*1000)