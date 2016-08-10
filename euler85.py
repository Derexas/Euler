import time, math

t = time.time()

def stuff(x, y):
	return x*y*(y+1)*(x+1)/4

target = 2000000
x = 1
y = 2000
result = [x,y]
while x < y:
	x += 1
	a = stuff(x,y)
	while a > target:
		y -= 1
		a = stuff(x,y)
	if abs(a - target) > abs(stuff(x,y+1) - target):
		a = stuff(x,y+1)
	if abs(a - target) < abs(stuff(result[0],result[1]) - target):
		result[0] = x
		result[1] = y

print(result[1]*result[0], time.time() - t)

"""
1: 1
2: 2+1 = 3
4: 4+2 + 2+1 = 9
6: 6+4+2 + 3+2+1 = 18
8: 8+6+4+2 + 4+3+2+1 = 30
9: 9+6+3 + 6+4+2 + 3+2+1 = 36
10: 10+8+6+4+2 + 5+4+3+2+1 = 45
12: 12+10+8+6+4+2 + 6+5+4+3+2+1 = 63 (6+5+4+3+2+1*(2+1))
 or 12+9+6+3 + 8+6+4+2 + 4+3+2+1 = 60
[...]
2 000 000: nope
1414²(nearest): (1414²+(1414-1)*1414+(1414-2)*1414+..)
	  1413/1414+(same /\)

x * y: x(y+(y-1)+(y-2)+..) + (x-1)(same) + ..
	 = sum(x to 1 of (y(y+1)/2))
	 = y/2*(y+1)*x/2*(x+1)
	 = xy(x+1)(y+1)/4
"""