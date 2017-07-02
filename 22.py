import time

t = time.time()

file = open('euler22_names.txt','r')

names = file.read().replace('"','').split(',')

print((time.time() - t) * 1000)
t = time.time()

names.sort()

print((time.time() - t) * 1000)
t = time.time()

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
		'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

total = 0
for i in range(len(names)):
    s = 0
    for letter in names[i]:
        s += letters.index(letter)+1
    total += s * (i + 1)
    
print(total, (time.time() - t) * 1000)
