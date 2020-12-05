# Read Input
f = open("input.txt", "r")

seatIds = []

for l in f:
	specification = l.strip()

	row = int(l[0:7].replace("F", "0").replace("B", "1"), 2)
	column = int(l[7:].replace("L", "0").replace("R", "1"), 2)
	seatId = row * 8 + column

	seatIds.append(seatId)

seatIds.sort()

for i in range(len(seatIds)):
	if i > 1:
		if seatIds[i - 1] == seatIds[i] - 2:
			print(seatIds[i - 1] + 1)