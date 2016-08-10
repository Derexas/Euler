import time, math

t = time.time()

n = 3
sqs = [str(x) for x in range(n)]

def nbcombinaisn(n, k): # (n+k-1)!/[k!*(n-1)!]
	denum = (math.factorial(k)*math.factorial(n-1))
	return math.factorial(n+k-1)/denum

def combinaison(k):
	a = 0
	bll = 1
	tab = [sqs]
	for l in range(k):
		tab.append([])
		t = []
		bl = 0
		ll = len(tab[l])
		for i in range(n):

			t += [sqs[i]+str(x) for x in tab[l][bl:ll]]
			#bl += 1#(n-1)**l
			print(bl)
		bll = bl
		tab[l+1] += t
		print(tab[l])
	print(len(tab[l]))


result = 0

result = nbcombinaisn(n, 4)
combinaison(4)

print(result, (time.time() - t)*1000)

#100-999 = 899
#100,101,102,..,111,..,199,..,578,..,999 = C(10,7)
#C(n,k) = (n+k-1)!/(k!(n-1)!)
#001,011,111,000
#00,01,02,03,11,12,13,22,23,33 = 4+3+2+1 = (4+2-1!)/2!(4-1)! = 10
#000,001,002,003,011,012,013,022,023,033,
#111,112,113,122,123,133,222,223,233,333
#(4+3+2+1)+(3+2+1)+(2+1)+(1) = (4+3-1)!/3!(4-1)! = 720/36 = 20

# 3: 0,1,2 ; 2(2*1-0),3(2*2-1) 
# 5: 0,1,2,3,4 ; 4(4*1-0),7(4*2-1),10(4*3-2)
# 5: 2,3,4 ; (2,3,4),6,(2,3,4),12,(3,4)
# 3: 