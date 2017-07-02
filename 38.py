import time

t = time.time()

digits = ['1','2','3','4','5','6','7','8','9']
l = 0

for i in range(1,9876):
	string = str(i)
	mult = 2
	while len(string) < 9:
		string += str(i*mult)
		mult += 1
	if len(string) == 9 and sorted(list(string)) == digits:
		sint = int(string)
		if sint > l:
			l = sint

print(l, time.time()-t, 's')
		

