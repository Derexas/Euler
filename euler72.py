import time, math

t = time.time()

def sieve(m):
    x = [True]*m
    x[0] = x[1] = False

    for i in range(2,int(math.sqrt(m))):
        j = 2*i
        while j < m:
            x[j] = False
            j = j+i

    return x

def primesinsieve(m):
    primes = []
    for i in range(len(m)):
        if m[i]:
            primes.append(i)
    return primes

def divisorsinprimes(m, p):
    d = [0]*m
    last = [1]*m
    for i in p:
        j = 2*i
        tt = (1 - 1/i)
        while j < m:
            d[j] += (j/i)*last[j]
            last[j] *= tt
            j = j+i
        if i > m//2:
            break
    for i in range(len(d)):
        if d[i] > 0:
            d[i] -= 1
    return d

result = 0

print(divisorsinprimes(14,[2,3,5,7,11,13]))

mm = 1000000
m = sieve(mm//2)
p = primesinsieve(m)

d = divisorsinprimes(mm, p)

print((mm-1)*mm/2 - (sum(d) - 1))

""" # Old version

def divisorsinl(m, l):
    d = [set() for _ in range(m)]
    for i in l:
        j = 2*i
        while j < m:
            d[j].add(i)
            j = j+i
    return d

stuff = False #switch between okay/long and notalreadyokay/short
mm = 1000000
m = sieve(mm//2)
p = primesinsieve(m)
#print(p)

result = 0
print(result, (time.time()-t)*1000)

m = mm
d = divisorsinl(m+1, p)

print(result, (time.time()-t)*1000)

prer = 0
for i in range(len(d)):
    o = 1
    oo = 0
    for e in d[i]:
        b = (i/e)*o
        oo += b
        o *= (1 - 1/e)
    if oo > 0:
        oo -= 1
    prer += oo
print(prer)
result = (m-1)*m/2 - prer
"""

""" # Old(test) version \/

def divisorsinl(m, l):
    d = [set() for _ in range(m)]

    for i in l:#(2,int(m/2)+1):
        j = 2*i
        k = [i]
        while j < m:
            d[j].update(k)
            if stuff:
                k.append(j)
            j = j+i

    return d

stuff = False #switch between okay/long and notalreadyokay/short
mm = 1000000
m = sieve(mm//2)
p = primesinsieve(m)
#print(p)

result = 0
print(result, (time.time()-t)*1000)

m = mm
d = divisorsinl(m+1, p)

print(result, (time.time()-t)*1000)

if m <= 30:
    print(d)
    if stuff:
        print([len(i) for i in d])

prer = 0
for i in range(len(d)):
    o = 1
    oo = 0
    for e in d[i]:
        if stuff:
            oo += 1
        else:
            b = (i/e)*o
            op = b#int(b/o) + b%o
            #should test for every other value and not their product
            #ex for 30: b = (30/5-1) ; b/3 + b%3 + b/2 + b%2
            if m <= 30:
                #print(i,e,op)
                pass

            oo += op
            #collisions (ex: 6 mult de 2 et 3)
        o *= (1 - 1/e)
    if not stuff:
        if oo > 0:
            oo -= 1
        #print(i,oo)
    prer += oo
print(prer)
result = (m-1)*m/2 - prer
"""

# old and unknow stuff \/
"""f = []*m
for i in range(m):
    f.append([])
for i in range(0,m):
    for e in d[i]:
        f[e].append(i)"""
#print(f)
"""
for i in range(m):
    e = d[i]
    for ee in e:
        for eee in f[ee]:
            if eee < i:
                e.append(eee)
            else:
                break"""
#print(d)


# really old and unknow stuff \/
"""
num = 1
den = 3
m = 1
f = 0

while den < 1200:
    den += 1
    num = den//3 + 1
    f = num/den
    if num/den == 1/3:
        num += 1
        f = num/den
    a = 0
    while f < 1/2:
        np = []
        for p in primes:
            if num + a % p == 0:
                np.append(p)
            if p*p > num:
                break
        prime = True
        for p in np:
            if den % p == 0:
                prime = False
                break
            if p*p > den:
                break
        if prime:
            result += 1
            
            #print(str(num + a)+'/'+str(den))
            """"""
        else:
            print(str(num)+'/'+str(den))
            print(np)""""""
        a += 1
        f = (num + a)/den"""

print(result, (time.time()-t)*1000)
