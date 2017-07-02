import time

t = time.time()

f = open("euler54_poker.txt", 'r')
pokerhands = (f.read()).split('\n')[:-1]
for i in range(len(pokerhands)):
	pokerhands[i] = pokerhands[i].split(' ')

vs = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
for i in range(2,10):
	vs[str(i)] = i

def handpower(cards):
	power = m = 0
	values = [0 for i in range(15)]
	suits = cards[0][1]
	rf = sf = f = True
	for card in cards:
		v = vs[card[0]]
		if v > m:
			m = v
		values[v] += 1
		if f and card[1] != suits:
			rf = sf = f = False
	concec = 0
	vv = 0
	for v in values:
		if v == 1:
			concec += 1
		elif v == 2:
			if power >= 300:
				power += 300
			elif power >= 100:
				if power - 100 < vv*3:
					power = 200 + vv*3
				else:
					power += 100
			else:
				power = 100 + vv*3
		elif v == 3:
			if power >= 100:
				power = 600
			else:
				power = 300
			power += 3*vv
		elif v == 4:
			power = 700 + vv*3
		elif concec < 5:
			concec = 0
		vv += 1
	if concec == 5:
		if values[-1] == 1:
			power = 900
		elif f:
			power = 800
		else:
			power = 400
	elif f:
		power = 500
	power += m/10
	return power

p1won = 0
for hands in pokerhands:
	if handpower(hands[:5]) > handpower(hands[5:]):
		p1won += 1

print(p1won, (time.time()-t)*1000)