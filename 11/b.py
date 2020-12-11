def printSeatPlan(seatPlan):
	for y in range(len(seatPlan)):
		line = ""

		for x in range(len(seatPlan[y])):
			line += seatPlan[y][x]

		print(line)

def countOccupiedNeighbors(seatPlan, x, y):
	neighbors = []
	occupiedNeighbors = 0

	tlFound = False
	tFound = False
	trFound = False
	lFound = False
	rFound = False
	blFound = False
	bFound = False
	brFound = False

	for i in range(1, max(len(seatPlan), len(seatPlan[0]))):
		if not tlFound and x - i >= 0 and y - i >= 0:
			if seatPlan[y - i][x - i] == OCCUPIED: 
				occupiedNeighbors += 1

			tlFound |= seatPlan[y - i][x - i] != FLOOR

		if not tFound and y - i >= 0:
			if seatPlan[y - i][x] == OCCUPIED:
				occupiedNeighbors += 1
				
			tFound |= seatPlan[y - i][x] != FLOOR

		if not trFound and x + i < len(seatPlan[0]) and y - i >= 0:
			if seatPlan[y - i][x + i] == OCCUPIED:
				occupiedNeighbors += 1
				
			trFound |= seatPlan[y - i][x + i] != FLOOR

		if not lFound and x - i >= 0:
			if seatPlan[y][x - i] == OCCUPIED:
				occupiedNeighbors += 1
			
			lFound |= seatPlan[y][x - i] != FLOOR

		if not rFound and x + i < len(seatPlan[0]):
			if seatPlan[y][x + i] == OCCUPIED:
				occupiedNeighbors += 1
			

			rFound |= seatPlan[y][x + i] != FLOOR

		if not blFound and x - i >= 0 and y + i < len(seatPlan):
			if seatPlan[y + i][x - i] == OCCUPIED:
				occupiedNeighbors += 1
				
			blFound |= seatPlan[y + i][x - i] != FLOOR

		if not bFound and y + i < len(seatPlan):
			if seatPlan[y + i][x] == OCCUPIED:
				occupiedNeighbors += 1
				
			bFound |= seatPlan[y + i][x] != FLOOR

		if not brFound and x + i < len(seatPlan[0]) and y + i < len(seatPlan):
			if seatPlan[y + i][x + i] == OCCUPIED:
				occupiedNeighbors += 1
			
			brFound |= seatPlan[y + i][x + i] != FLOOR

		if tlFound and tFound and trFound and lFound and rFound and blFound and bFound and brFound:
			break

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
			elif seatPlan[y][x] == OCCUPIED and countOccupiedNeighbors(seatPlan, x, y) >= 5:
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