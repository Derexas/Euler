
import time

t = time.time()

def isprime(n):
    i = 0
    prime = True
    while primes[i]**2 <= n:
        if n % primes[i] == 0:
            prime = False
            break
        i += 1
    return prime

primes = [2]
n = 3
while primes[-1] < 5000:    
    if isprime(n):
        primes.append(n)
    n += 2

maxcp = 2
maxcpp = maxcpb = 0
i = j = s = 0
t = time.time()
while i+j < len(primes):
    while s < 1000000 and i+j < len(primes):
        if j > maxcp and isprime(s):
                maxcp = j
                maxcpp = s
                maxcpb = i
        s += primes[i+j]
        j += 1
    s -= primes[i]
    j -= 1
    while s >= 1000000:
        s -= primes[i+j]
        j -= 1
    i += 1

print(maxcp, maxcpp, (time.time()-t)*1000)


