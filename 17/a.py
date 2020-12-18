import copy

def countActiveNeighbors(state, posX, posY, posZ):
	activeCount = 0

	for x in range(posX - 1, posX + 2):
		for y in range(posY - 1, posY + 2):
			for z in range(posZ - 1, posZ + 2):
				if not (x == posX and y == posY and z == posZ):
					if state.get(z, {}).get(y, {}).get(x, INACTIVE) == ACTIVE:
						activeCount += 1

	return activeCount

def printState(state, minX, maxX, minY, maxY, minZ, maxZ):
	for z in range(minZ, maxZ):
		print("z=" + str(z))

		for y in range(minY, maxY):
			line = ""

			for x in range(minX, maxX):
				line += state[z][y][x]

			print(line)

		print()

# Read Input
f = open("input.txt", "r")

ACTIVE = "#"
INACTIVE = "."

z = 0
y = 0
state = {}

minZ = 0
maxZ = 1
minY = 0
maxY = 0
minX = 0
maxX = 0

state[z] = {}

for line in f:
	state[z][y] = {}
	x = 0

	for c in line.strip():
		state[z][y][x] = c
		x += 1

	maxX = x
	y += 1

maxY = y

# print("INITIAL:")
# printState(state, minX, maxX, minY, maxY, minZ, maxZ)
# print("X: " + str(minX) + ", " + str(maxX) + ", Y: " + str(minY) + ", " + str(maxY) + ", Z: " + str(minZ) + ", " + str(maxZ))

for cycle in range(0, 6):
	newState = copy.deepcopy(state)

	minActiveX = 0
	maxActiveX = 0
	minActiveY = 0
	maxActiveY = 0
	minActiveZ = 0
	maxActiveZ = 0

	activeCubes = 0

	for z in range(minZ - 1, maxZ + 1):
		newState[z] = {}

		for y in range(minY - 1, maxY + 1):
			newState[z][y] = {}

			for x in range(minX - 1, maxX + 1):
				activeNeighbors = countActiveNeighbors(state, x, y, z)
				posState = state.get(z, {}).get(y, {}).get(x, INACTIVE)

				if posState == ACTIVE:
					if activeNeighbors == 2 or activeNeighbors == 3:
						newState[z][y][x] = ACTIVE

						if z < minActiveZ: minActiveZ = z
						if z > maxActiveZ: maxActiveZ = z
						if y < minActiveY: minActiveY = y
						if y > maxActiveY: maxActiveY = y
						if x < minActiveX: minActiveX = x
						if x > maxActiveX: maxActiveX = x

						activeCubes += 1
					else:
						newState[z][y][x] = INACTIVE
				elif posState == INACTIVE:
					if activeNeighbors == 3:
						newState[z][y][x] = ACTIVE

						if z < minActiveZ: minActiveZ = z
						if z > maxActiveZ: maxActiveZ = z
						if y < minActiveY: minActiveY = y
						if y > maxActiveY: maxActiveY = y
						if x < minActiveX: minActiveX = x
						if x > maxActiveX: maxActiveX = x

						activeCubes += 1
					else:
						newState[z][y][x] = INACTIVE

	minX = minActiveX
	minY = minActiveY
	minZ = minActiveZ
	maxX = maxActiveX + 1
	maxY = maxActiveY + 1
	maxZ = maxActiveZ + 1
	state = copy.deepcopy(newState)

	# print("AFTER CYCLE " + str(cycle) + ":")
	# printState(state, minX, maxX, minY, maxY, minZ, maxZ)
	# print("X: " + str(minX) + ", " + str(maxX) + ", Y: " + str(minY) + ", " + str(maxY) + ", Z: " + str(minZ) + ", " + str(maxZ))

print(activeCubes)