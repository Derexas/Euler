import time

t = time.time()

f = open("euler59_cipher.txt", 'r')
fstring = f.read()
flist = fstring.split(',')

result = 0

key = [0,0,0]
for i in range(3):
	newlist = []
	for j in range(i, len(flist), 3):
		newlist.append(flist[j])
	mostcommon = max(set(newlist), key=newlist.count)
	key[i] = int(mostcommon)^32

print('key:', key)
j = 0
for i in range(len(flist)):
	result += int(flist[i])^key[j]
	j += 1
	if j == 3:
		j = 0

print(result, (time.time()-t)*1000)
