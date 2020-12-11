def printSeatPlan(seatPlan):
	for y in range(len(seatPlan)):
		line = ""

		for x in range(len(seatPlan[y])):
			line += seatPlan[y][x]

		print(line)

def countOccupiedNeighbors(seatPlan, x, y):
	neighbors = []
	occupiedNeighbors = 0

	for ry in range(y - 1, y + 2):
		for rx in range(x - 1, x + 2):
			if ry >= 0 and ry < len(seatPlan) and rx >= 0 and rx < len(seatPlan[y]) and (ry != y or rx != x):
				if seatPlan[ry][rx] == OCCUPIED: occupiedNeighbors += 1

	return occupiedNeighbors

# Read Input
f = open("input.txt", "r")

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

seatPlan = []
y = 0

for l in f:
	seatPlan.append([])

	for c in l.strip():
		seatPlan[y].append(c)

	y += 1

printSeatPlan(seatPlan)

changesDetected = True

while changesDetected:
	newSeatPlan = []
	changesDetected = False

	for y in range(len(seatPlan)):
		newSeatPlan.append([])

		for x in range(len(seatPlan[y])):
			if seatPlan[y][x] == EMPTY and countOccupiedNeighbors(seatPlan, x, y) == 0:
				newSeatPlan[y].append(OCCUPIED)
				changesDetected = True
			elif seatPlan[y][x] == OCCUPIED and countOccupiedNeighbors(seatPlan, x, y) >= 4:
				newSeatPlan[y].append(EMPTY)
				changesDetected = True
			else:
				newSeatPlan[y].append(seatPlan[y][x])

	seatPlan = newSeatPlan

print("---")
printSeatPlan(seatPlan)

occupiedSeats = 0

for row in seatPlan:
	for seat in row:
		if seat == OCCUPIED: occupiedSeats += 1

print("---")
print(occupiedSeats)