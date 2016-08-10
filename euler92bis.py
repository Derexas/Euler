import time, math

t = time.time()
result = 0

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def ff(n):
	ch = ''
	ret = r = 0
	for c in n:
		if c != ch:
			r += 1
			ch = c
	return nCr(len(n),r)

def function(cur_v, cur_i, st, a=""):
	global result
	#print(a, "'"+st+"'", cur_i, sqrs[cur_i], cur_v)
	if cur_v - sqrs[cur_i] >= 0:
		st += str(cur_i+1)
		if len(st) > 7:
			return
		cur_v -= sqrs[cur_i]
		if cur_v == 0:
			if int(st) < 9*9*7:
				blah(int(st))
			else:
				print("                                    ",int(st))
				result += ff(st)
		if cur_i >= 0:
			for i in range(cur_i, -1, -1):
				function(cur_v, i, st, a+" ")

def blah(N):
	for i in range(sqrs_la, 0, -1):
		st = ""
		n = N
		function(n, i, st)

sqrs = [x*x for x in range(1,10)]
N = 100
sqrs_la = len(sqrs) - 1
blah(N)

print(result, time.time()-t, ff('999551'))

# Reste à trouver le nombre d'organisations possibles des nombres trouvés

"""
991
919
199

9912
9921
9192
9291
1929
2919
1299
2199
1992
2991
"""