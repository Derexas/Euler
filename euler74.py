import time, math

t = time.time()

def factofdigits(n):
    s = 0
    while n > 0:
        nn = n//10
        s += facts[n - nn*10]
        n = nn
    return s

def stuff(n, p):
    if p == 0:
        nextstuff.append(n)
    else:
        if n > 0:
            stuff(n + facts[0], p - 1)
        else:
            stuff(n, p - 1)
        for i in range(1,10):
            stuff(n + facts[i], p - 1)

M = 1000000
result = 0
#chains = [0 for i in range(4*M)]
facts = [math.factorial(i) for i in range(0, 10)]

nextstuff = []
stuff(0, 6)

for i in range(M//10):
    a = 1
    n = i
    l = []
    while not n in l:
        l.append(n)
        if n < M:
            n = nextstuff[n]
        else:
            n = factofdigits(n)
        a += 1
    if a == 60:
        #print(str(i) + ' ' + str(a))
        result += 1

"""
for i in range(M//1000):
    if chains[i] > 0:
        ll = chains[i]        
    else:
        n = i
        subchain = [i]
        while True:
            #print(n)
            if n < M:
                r = nextstuff[n]
            else:
                r = factofdigits(n)
            if False:#r < M and chains[r] > 0:
                ll = len(subchain) + chains[r]
                break
            elif r in subchain:
                ll = len(subchain)
                break
            else:
                subchain.append(r)
            n = r
        for i in subchain:
            chains[i] = ll
    #print('='+str(ll))
    #print('---------------------')
    if ll == 5:
        result += 1
        print(str(i))"""

print(result, (time.time()-t)*1000)
