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

waypointX = 10
waypointY = -1

for l in f:
	action = l[0]
	value = int(l[1:])

	if action == actionNorth:
		waypointY -= value
	elif action == actionSouth:
		waypointY += value
	elif action == actionEast:
		waypointX += value
	elif action == actionWest:
		waypointX -= value
	elif action == actionLeft:
		if value == 90:
			tmp = waypointX
			waypointX = waypointY
			waypointY = -tmp
		elif value == 180:
			waypointX *= -1
			waypointY *= -1
		elif value == 270:
			tmp = waypointX
			waypointX = -waypointY
			waypointY = tmp
	elif action == actionRight:
		if value == 90:
			tmp = waypointX
			waypointX = -waypointY
			waypointY = tmp
		elif value == 180:
			waypointX *= -1
			waypointY *= -1
		elif value == 270:
			tmp = waypointX
			waypointX = waypointY
			waypointY = -tmp
	elif action == actionForward:
		x += waypointX * value
		y += waypointY * value

print(abs(x - startX) + abs(y - startY))