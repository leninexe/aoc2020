# Read Input
f = open("input.txt", "r")

maxSeatId = 0

for l in f:
	specification = l.strip()

	row = int(l[0:7].replace("F", "0").replace("B", "1"), 2)
	column = int(l[7:].replace("L", "0").replace("R", "1"), 2)
	seatId = row * 8 + column

	if seatId > maxSeatId: maxSeatId = seatId

print(maxSeatId)