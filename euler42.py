import time

t = time.time()

file = open('euler42_words.txt','r')

words = file.read().replace('"','').split(',')

print((time.time() - t) * 1000)
t = time.time()

result = 0

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
		'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
trianglesn = []
for i in range(1,20):
	trianglesn.append(int(0.5*i*(i+1)))

for word in words:
	summ = 0
	for letter in list(word):
		summ += letters.index(letter)+1
	if summ in trianglesn:
		result += 1

print(result, (time.time() - t) * 1000)
