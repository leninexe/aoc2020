import copy

def countActiveNeighbors(state, posX, posY, posZ, posW):
	activeCount = 0

	for x in range(posX - 1, posX + 2):
		for y in range(posY - 1, posY + 2):
			for z in range(posZ - 1, posZ + 2):
				for w in range(posW - 1, posW + 2):
					if not (x == posX and y == posY and z == posZ and w == posW):
						if state.get(w, {}).get(z, {}).get(y, {}).get(x, INACTIVE) == ACTIVE:
							activeCount += 1

	return activeCount

def printState(state, minX, maxX, minY, maxY, minZ, maxZ, minW, maxW):
	for w in range(minW, maxW):
		for z in range(minZ, maxZ):
			print("z=" + str(z) + ", w=" + str(w))

			for y in range(minY, maxY):
				line = ""

				for x in range(minX, maxX):
					line += state[w][z][y][x]

				print(line)

			print()

# Read Input
f = open("input.txt", "r")

ACTIVE = "#"
INACTIVE = "."

w = 0
z = 0
y = 0
state = {}

minW = 0
maxW = 1
minZ = 0
maxZ = 1
minY = 0
maxY = 0
minX = 0
maxX = 0

state[w] = {}
state[w][z] = {}

for line in f:
	state[w][z][y] = {}
	x = 0

	for c in line.strip():
		state[w][z][y][x] = c
		x += 1

	maxX = x
	y += 1

maxY = y

# print("INITIAL:")
# printState(state, minX, maxX, minY, maxY, minZ, maxZ, minW, maxW)
# print("X: " + str(minX) + ", " + str(maxX) + ", Y: " + str(minY) + ", " + str(maxY) + ", Z: " + str(minZ) + ", " + str(maxZ) + ", W: " + str(minW) + ", " + str(maxW))

for cycle in range(0, 6):
	newState = copy.deepcopy(state)

	minActiveX = 0
	maxActiveX = 0
	minActiveY = 0
	maxActiveY = 0
	minActiveZ = 0
	maxActiveZ = 0
	minActiveW = 0
	maxActiveW = 0

	activeCubes = 0

	for w in range(minW - 1, maxW + 1):
		newState[w] = {}

		for z in range(minZ - 1, maxZ + 1):
			newState[w][z] = {}

			for y in range(minY - 1, maxY + 1):
				newState[w][z][y] = {}

				for x in range(minX - 1, maxX + 1):
					activeNeighbors = countActiveNeighbors(state, x, y, z, w)
					posState = state.get(w, {}).get(z, {}).get(y, {}).get(x, INACTIVE)

					# print("[" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + "]: " + str(activeNeighbors))

					if posState == ACTIVE:
						if activeNeighbors == 2 or activeNeighbors == 3:
							newState[w][z][y][x] = ACTIVE

							if w < minActiveW: minActiveW = w
							if w > maxActiveW: maxActiveW = w
							if z < minActiveZ: minActiveZ = z
							if z > maxActiveZ: maxActiveZ = z
							if y < minActiveY: minActiveY = y
							if y > maxActiveY: maxActiveY = y
							if x < minActiveX: minActiveX = x
							if x > maxActiveX: maxActiveX = x

							activeCubes += 1
						else:
							newState[w][z][y][x] = INACTIVE
					elif posState == INACTIVE:
						if activeNeighbors == 3:
							newState[w][z][y][x] = ACTIVE

							if w < minActiveW: minActiveW = w
							if w > maxActiveW: maxActiveW = w
							if z < minActiveZ: minActiveZ = z
							if z > maxActiveZ: maxActiveZ = z
							if y < minActiveY: minActiveY = y
							if y > maxActiveY: maxActiveY = y
							if x < minActiveX: minActiveX = x
							if x > maxActiveX: maxActiveX = x

							activeCubes += 1
						else:
							newState[w][z][y][x] = INACTIVE

	minX = minActiveX
	minY = minActiveY
	minZ = minActiveZ
	minW = minActiveW
	maxX = maxActiveX + 1
	maxY = maxActiveY + 1
	maxZ = maxActiveZ + 1
	maxW = maxActiveW + 1
	state = copy.deepcopy(newState)

	# print("AFTER CYCLE " + str(cycle) + ":")
	# printState(state, minX, maxX, minY, maxY, minZ, maxZ, minW, maxW)
	# print("X: " + str(minX) + ", " + str(maxX) + ", Y: " + str(minY) + ", " + str(maxY) + ", Z: " + str(minZ) + ", " + str(maxZ) + ", W: " + str(minW) + ", " + str(maxW))

print(activeCubes)