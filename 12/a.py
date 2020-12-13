# Read Input
f = open("input.txt", "r")

actionNorth = "N"
actionSouth = "S"
actionEast = "E"
actionWest = "W"
actionLeft = "L"
actionRight = "R"
actionForward = "F"

directionNorth = 0
directionEast = 1
directionSouth = 2
directionWest = 3

direction = directionEast
startX = 0
startY = 0
x = startX
y = startY

for l in f:
	action = l[0]
	value = int(l[1:])

	if action == actionNorth:
		y -= value
	elif action == actionSouth:
		y += value
	elif action == actionEast:
		x += value
	elif action == actionWest:
		x -= value
	elif action == actionLeft:
		direction -= value / 90
		direction %= 4
	elif action == actionRight:
		direction += value / 90
		direction %= 4
	elif action == actionForward:
		if direction == directionNorth:
			y -= value
		elif direction == directionEast:
			x += value
		elif direction == directionSouth:
			y += value
		elif direction == directionWest:
			x -= value

print(abs(x - startX) + abs(y - startY))